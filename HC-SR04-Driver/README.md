# HC-SR04-RangeFinder
This program read distance from ultrasonic sensor HC-SR04 and send it to arducopter (PX4, APM) on serial. 
## Program description
Pixhawk distance read rate is 20Hz. If pixhawk send something on serial, arduino repty distance in format "12.34\r\n" in meters.
From HC-SR04 you can read distance every 30ms (about 33Hz). Arduino read the distance and do some math. You can set MODE, MEDIAN, SPIKE, NORM filter. 

# Ardurover settings:

Serial comunication is same as LightWare SF10, so on ardurover use same settings  - http://ardupilot.org/rover/docs/common-lightware-sf10-lidar.html

SERIAL4_PROTOCOL = 9 (Lidar)

SERIAL4_BAUD = 19 (19200 baud)

RNGFND_TYPE = 8 (LightWareSerial)

RNGFND_SCALING = 1

RNGFND_MIN_CM = 5

RNGFND_MAX_CM = 300 

RNGFND_GNDCLEAR = 3 or more accurately the distance in centimetres from the range finder to the ground when the vehicle is landed. This value depends on how you have mounted the rangefinder.


# Conection:
## Arduino pin <-> HC-SR04
3 - Trigger

2 - Echo


Sonar pinouts fits in to arduino mini pro. There is in alongside gnd,pin 2, pin 3, pin 4. On sonar is gnd, echo, trigger, supply. So only you need connect pin 4 to vcc.

## Arduino <-> ardurover (pixhawk)
Gnd - Gnd

Vcc - Vcc   (5V) 

Rx - Tx

Tx - Rx


ardupilot.org/rover/docs/common-lightware-sf10-lidar.html

