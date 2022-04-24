import tkinter
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

redLedPinId = 23
greenLedPinId = 24
blueLedPinId = 25

GPIO.setup(redLedPinId,GPIO.OUT)
GPIO.setup(greenLedPinId,GPIO.OUT)
GPIO.setup(blueLedPinId,GPIO.OUT)

win = tkinter.Tk()
win.title("LED CONTROLLER")
win.minsize(500, 500)

def quitFunc():
    turnOffAllLeds()
    GPIO.cleanup()
    win.destroy()

quitBtn = tkinter.Button(win, text="Quit", command=quitFunc)
quitBtn.pack()

def turnOffAllLeds():
    print("Turning off all LEDs")
    GPIO.output(redLedPinId, GPIO.LOW)
    GPIO.output(greenLedPinId, GPIO.LOW)
    GPIO.output(blueLedPinId, GPIO.LOW)

def turnOnRedLed():
    turnOffAllLeds()
    print("Turning on red LED")
    GPIO.output(redLedPinId, GPIO.HIGH)


redLedBtn = tkinter.Button(win, text="Turn on red LED", command=turnOnRedLed)
redLedBtn.pack()

def turnOnGreenLed():
    turnOffAllLeds()
    print("Turning on green LED")
    GPIO.output(greenLedPinId, GPIO.HIGH)

greenLedBtn = tkinter.Button(win, text="Turn on green LED", command=turnOnGreenLed)
greenLedBtn.pack()

def turnOnBlueLed():
    turnOffAllLeds()
    print("Turning on blue LED")
    GPIO.output(blueLedPinId, GPIO.HIGH)
    
blueLedBtn = tkinter.Button(win, text="Turn on blue LED", command=turnOnBlueLed)
blueLedBtn.pack()

win.mainloop()