import os
from flask import Flask
from azure.servicebus import QueueClient, Message

queue_client = QueueClient.from_connection_string(os.getenv('SERVICEBUS_CONN_STRING'), 'request')
queue_receiver = queue_client.get_receiver()
app = Flask(__name__)

def get_command_servicebus(queue_receiver):
    messages = queue_receiver.fetch_next(timeout=3)
    if messages:
        for message in messages:
            print(message)
            message.complete()
            return str(message)
    else:
        print("The queue is empty")
        return ''

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/pull")
def pull():
    return get_command_servicebus(queue_receiver)

