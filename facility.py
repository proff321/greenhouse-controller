import gpiozero

FAN_PIN = 1
HEATER_PIN = 2
LIGHT_PIN = 3

def getTemp():
    return 12

def getFanDevice():
    return gpiozero.OutputDevice(FAN_PIN)

def getHeaterDevice():
    return gpiozero.OutputDevice(HEATER_PIN)

def getLightDevice():
    return gpiozero.OutputDevice(LIGHT_PIN)

def fanOn():
    device = getFanDevice()
    device.on()
    return

def fanOff():
    device = getFanDevice()
    device.off()
    return

def heaterOn():
    device = getHeaterDevice()
    device.on()
    return

def heaterOff():
    device = getHeaterDevice()
    device.off()
    return

def lightOn():
    device = getLightDevice()
    device.on()
    return

def lightOff():
    device = getLightDevice()
    device.off()
    return

