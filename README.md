# led-lanyard

## Introduction

My friend [Dan Stach](https://github.com/DanStach/rpi-ws2811) was the inspiration behind all of this.  From his prototype and with help from [Bricks and Minifigs of Dallas, TX](https://www.facebook.com/BAMNorthDallas/), we built the first [LEGO LED lanyard + badge holder](https://twitter.com/lastcoolname/status/1136092293801418753).  I've since extended it to be RaspberryPi controlled with the intent to Open Source/Package the design.

## Parts

If you want, you can purchase the components individually and assemble yourself.  If there's enough interest, I will offer a packaged solution.

* [Wireless RF LED RGP Controller](https://amzn.to/2WrNkZ1)
* [WS2812B RGB LED Strip 144 pixels](https://amzn.to/2Whalc4) - This is where the magic happens.  
* [5.5mm x 2.1mm Barrel Jack to USB DC Cable](https://amzn.to/2XrmtZn)
* [Portable battery](https://amzn.to/2XzPceK) - You can use an existing power bank if you don't want to purchase
* [Tubular Polyester Webbing](https://www.strapworks.com/product_p/stpw1.htm) - You'll need at least 4 feet.  White diffuses the light better, but black gives it a more 8-bit aesthetic. 
* Hot Glue Gun + Hot Glue
* Matches/open flame
* LEGO.  Lots of 1 width Technic LEGO bricks.  Preferably, the same color as your webbing.

## Organization

This repo is broken up into three parts (directories):

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
