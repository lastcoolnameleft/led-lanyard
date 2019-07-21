# LED Lanyard

This project is for the design and reference for building of an LED lanyard, primarily used in conferences.

## Background

[Dan Stach](https://github.com/DanStach/), the original creator of the LED lanyard, build a prototype for his work badge using his X-mas tree neopixel creation.  Extending this design,  I worked with [Bricks and Minifigs of Dallas, TX](https://www.facebook.com/BAMNorthDallas/), to build the first [LEGO LED lanyard + badge holder](https://twitter.com/lastcoolname/status/1136092293801418753).  I posted this to Twitter which receive a tremendous amount of attention, so this repo is intended to host build and extention details for the LED Lanyard.

The original design utilized an Neopixels with an RF hardware controller.  With Dan's help, we've extended it to run on a RaspberryPi + Python.

## Getting started

This repo is broken up into parts:

* [Parts](docs/parts.md) - If you are interested in building your own, this is the Build Of Materials (BOM).
* [Assembly](docs/assembly.md) - After you have all of the parts, you will need to assemble them.
* [Extending with Raspberry Pi](docs/raspberrypi.md) - The RF controller has pre-programmed effects; however, if you want to program your own, you can use your own controller.  I have created some examples with integrations to [Twilio](https://www.twilio.com/) and [Azure Bot Framework](https://azure.microsoft.com/en-us/services/bot-service/).

## Related Efforts

* [Dan Stach's RPI WS2811 code](https://github.com/DanStach/rpi-ws2811)

## License

[MIT](license.md) © Tommy Falgout