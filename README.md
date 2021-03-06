## Python Interface for the ArcBotics Hexy Robot

[![Build Status](https://travis-ci.org/mluds/hexapod.svg?branch=master)](https://travis-ci.org/mluds/hexapod)

`hexapod` interacts with the [Hexy robot from Arcbotics](http://arcbotics.com/products/hexy/).

### Setup and Installation

1. Build your robot following [these instructions](http://arcbotics.com/products/hexy/start/building-your-hexy-the-hexapod/).
2. Connect the Arduino to your computer via a serial connection.
3. Download the [Hexy firmware](http://arcbotics.com/hosting/Servotor32/Servotor32_2v0.zip); then install it using the [Arduino IDE](https://www.arduino.cc/en/Main/Software).
4. Install [Python 3](https://docs.python.org/3/using/index.html), preferably on a Linux machine.
5. Run `sudo pip install -e git+https://github.com/mluds/hexapod.git#egg=hexapod` to install this package.
6. Run `sudo hexapod-test` to see if everything works.
