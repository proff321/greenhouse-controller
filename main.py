#!/usr/bin/python
import facility

SET_POINT = 70
DELTA = 5

def tempDiff():
    return facility.getTemp() - SET_POINT

def shouldEnableHeater():
    return (tempDiff() + DELTA) < 0

if (shouldEnableHeater()) :
    facility.heaterOn()
else:
    facility.heaterOff()
