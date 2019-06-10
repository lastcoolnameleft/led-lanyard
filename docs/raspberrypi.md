# Raspberry Pi

Here are the components necessary for using a RaspberryPi to control the LED Lanayrd:

* lanyard - The base component.  Listens for commands.
* twilio - Receives command from twilio
* azure-bot - Reveives commands from the Azure Bot Framework

## Installation

Each directory has a `install.sh` script used to install and setup that component

## Lanyard component

This periodically pulls the top line from a file to determine which LED configuration it should use.  

### Lanyard effects

The `lanyard/effects/ws2811.py` file contains most of the math/algorithms for using the different LED configurations.

## Twilio

If you want to interact with the lanyard via Twilio, you can specify your twilio details and texts sent to your phone number will be added to the message queue.

## Azure Bot Framework

If you want to interact with the lanyard via the Azure Bot Framework, you can specify your Azure Bot Framework connection details and any messages sent to the bot will be added to the message queue.
