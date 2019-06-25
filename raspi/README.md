# Automation code for CPX drum machine using Appium Rasbperry Pi driver

This module contains an Appium test designed to be run against a running [appium-raspi-driver](https://github.com/jlipps/appium-raspi-driver). The test plays a sequence of drum hits. See `test.js` for the code. The assumption made there is that the Appium server is running at `http://raspberrypi.local:7774`.

### Installation

Git clone, then `npm install`

### Run the test

```
node test.js
```
