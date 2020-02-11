import http.server
import json
import asyncio
import ssl
from botbuilder.schema import (Activity, ActivityTypes, ChannelAccount)
from botframework.connector import ConnectorClient
from botframework.connector.auth import (MicrosoftAppCredentials,
                                         JwtTokenValidation, SimpleCredentialProvider)
import os

bot_app_id = os.getenv('BOT_APP_ID')
bot_app_password = os.getenv('BOT_APP_PASSWORD')
queue_file = os.getenv('QUEUE_FILE')

print('bot_app_id=' + bot_app_id)
print('bot_app_password=' + bot_app_password)
if not bot_app_id or not bot_app_password or not queue_file:
    exit('Must set env vars for: BOT_APP_ID, BOT_APP_PASSWORD and QUEUE_FILE')

allowed_actions = ['blue', 'red', 'green', 'black', 'fill-random', 'msft', 'fadeinout', 'chase', 'follow', 'fire', 'level-colors', 'sparkle', 'cylon']

class BotRequestHandler(http.server.BaseHTTPRequestHandler):

    @staticmethod
    def __create_reply_activity(request_activity, text):
        return Activity(
            type=ActivityTypes.message,
            channel_id=request_activity.channel_id,
            conversation=request_activity.conversation,
            recipient=request_activity.from_property,
            from_property=request_activity.recipient,
            text=text,
            service_url=request_activity.service_url)

    def __handle_conversation_update_activity(self, activity):
        self.send_response(202)
        self.end_headers()
        if activity.members_added[0].id != activity.recipient.id:
            credentials = MicrosoftAppCredentials(bot_app_id, bot_app_password)
            reply = BotRequestHandler.__create_reply_activity(activity, 'Hello and welcome to the lanyard bot!')
            connector = ConnectorClient(credentials, base_url=reply.service_url)
            connector.conversations.send_to_conversation(reply.conversation.id, reply)

    def __handle_message_activity(self, activity):
        self.send_response(200)
        self.end_headers()
        credentials = MicrosoftAppCredentials(bot_app_id, bot_app_password)
        connector = ConnectorClient(credentials, base_url=activity.service_url)
        response = BotRequestHandler.process_message(activity.text)
        reply = BotRequestHandler.__create_reply_activity(activity, response)
        connector.conversations.send_to_conversation(reply.conversation.id, reply)

    def __handle_authentication(self, activity):
        credential_provider = SimpleCredentialProvider(bot_app_id, bot_app_password)
        loop = asyncio.new_event_loop()
        try:
            loop.run_until_complete(JwtTokenValidation.authenticate_request(
                activity, self.headers.get("Authorization"), credential_provider))
            return True
        except Exception as ex:
            self.send_response(401, ex)
            self.end_headers()
            return False
        finally:
            loop.close()

    def __unhandled_activity(self):
        self.send_response(404)
        self.end_headers()

    def do_POST(self):
        body = self.rfile.read(int(self.headers['Content-Length']))
        data = json.loads(str(body, 'utf-8'))
        activity = Activity.deserialize(data)

        if not self.__handle_authentication(activity):
            return

        if activity.type == ActivityTypes.conversation_update.value:
            self.__handle_conversation_update_activity(activity)
        elif activity.type == ActivityTypes.message.value:
            self.__handle_message_activity(activity)
        else:
            self.__unhandled_activity()

    # Lanyard code
    @staticmethod
    def add_to_file(message):
        with open(queue_file, 'a') as file:
            file.write(message + "\n")
        file.close()

    @staticmethod
    def process_message(message):
        message = message.lower()
        response = ''
        if message not in allowed_actions:
            response = "I did not recognize that value.  Try one of the following:" + str(allowed_actions)
        else:
            BotRequestHandler.add_to_file(message)
            response = "Your request has been added to the queue."
        return response

try:
    SERVER = http.server.HTTPServer(('0.0.0.0', 9000), BotRequestHandler)
    print('Started http server')
    SERVER.serve_forever()
except KeyboardInterrupt:
    print('^C received, shutting down server')
    SERVER.socket.close()
