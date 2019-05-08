from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os

# Create the QueueClient
queue_file = '/tmp/messages.queue'
app = Flask(__name__)

allowed_settings = ['blue', 'red', 'green', 'black', 'fill-random', 'msft', 'fadeinout', 'chase', 'follow', 'fire', 'level-colors', 'sparkle', 'cylon']

def add_to_file(message):
    with open(queue_file, 'a') as file:
        file.write(message + "\n")
    file.close()

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    #number = request.form['From']
    message_body = request.form['Body'].lower()
    #msg = Message(b'Test Message')
    resp = MessagingResponse()
    if message_body not in allowed_settings:
        resp.message("I did not recognize that value.  Try one of the following:" + str(allowed_settings))
    else:
        add_to_file(message_body)
        resp.message("Your request has been added to the queue.")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)