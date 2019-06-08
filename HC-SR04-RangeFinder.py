import serial as Serial
import statistics as stat
import struct
import ObstacleDetectionTRR as detect
from sys_clock import millis as sys_millis

lastT = 0
updateTime = 30  # Time between sonar reads

STBY_MODE = 0
NORM_MODE = 1
MODE_MODE = 2
MEDN_MODE = 3
SPIKE_MODE = 4

SPIKE_EFFECT = 4.0
ARRAY_SIZE = 5

MIN_RANGE = 1
MAX_RANGE = 320


def getCm():
    return detect.distance()[3]


def millis():
    return sys_millis()


def loop():
    VAL = 0

    # For Mode/median filter variables needed to store values
    # array to store the raw samples
    rawValues = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Array to store the sorted samples
    srtValues = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    # index for the latest position in array
    IDX = 0

    serial = Serial.Serial('/dev/ttyAMA0', baudrate=19200, timeout=updateTime)
    filtMode = MODE_MODE

    while True:
        lastT = millis()
        nowT = millis()
        tmp = getCm()

        if tmp > MAX_RANGE:
            tmp = MAX_RANGE

        if tmp < MIN_RANGE:
            tmp = 0

        if filtMode == NORM_MODE:
            VAL = tmp

        elif filtMode == MODE_MODE:
            rawValues[IDX] = tmp
            IDX += 1

            if IDX >= ARRAY_SIZE:
                IDX = 0

            for i in range(ARRAY_SIZE):
                srtValues[i] = rawValues[i]

            srtValues.sort()
            try:
                VAL = stat.mode(srtValues)
            except stat.StatisticsError as e:
                VAL = tmp

        elif filtMode == MEDN_MODE:
            rawValues[IDX] = tmp
            IDX += 1
            if IDX >= ARRAY_SIZE:
                IDX = 0

            for i in range(ARRAY_SIZE):
                srtValues[i] = rawValues[i]

            srtValues.sort()
            VAL = stat.median()

        else:
            lastT = nowT

        # Investigate the rest of the modes. we might not need them.

        if serial.is_open:
            # Read the incoming byte
            _ = serial.read()

            # Process the float value and servie to the pixhawk over serial ports...
            floatm = float(VAL)
            ieee754_data = struct.pack('f', floatm)

            serial.write(ieee754_data)
