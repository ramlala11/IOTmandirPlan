import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD) #set the Pin mode you will be working with
ledPin1 = 15 #this is GPIO22 pin i.e Physical Pin15
ledPin2 = 16
ledPin3 = 18
ledPin4 = 22
ledPin5 = 33
ledPin6 = 36
ledPin7 = 38
ledPin8 = 40


#setup the ledPin(i.e. GPIO22) as output
GPIO.setup(ledPin1, GPIO.OUT)
GPIO.setup(ledPin2, GPIO.OUT)
GPIO.setup(ledPin3, GPIO.OUT)
GPIO.setup(ledPin4, GPIO.OUT)
GPIO.setup(ledPin5, GPIO.OUT)
GPIO.setup(ledPin6, GPIO.OUT)
GPIO.setup(ledPin7, GPIO.OUT)
GPIO.setup(ledPin8, GPIO.OUT)

GPIO.output(ledPin1, False)
GPIO.output(ledPin2, False)
GPIO.output(ledPin3, False)
GPIO.output(ledPin4, False)
GPIO.output(ledPin5, False)
GPIO.output(ledPin6, False)
GPIO.output(ledPin7, False)
GPIO.output(ledPin8, False)

def fn1():
    try:
        while True:
            GPIO.output(ledPin1, True) #Set the LED Pin to HIGH
            GPIO.output(ledPin2, True)
            GPIO.output(ledPin3, True)
            GPIO.output(ledPin4, True)
            GPIO.output(ledPin5, True)
            GPIO.output(ledPin6, True)
            GPIO.output(ledPin7, True)
            GPIO.output(ledPin8, True)
            print("LED ON")
            sleep(1) #Wait for 1 sec
            GPIO.output(ledPin1, False) #Set the LED Pin to LOW
            GPIO.output(ledPin2, False)
            GPIO.output(ledPin3, False)
            GPIO.output(ledPin4, False)
            GPIO.output(ledPin5, False)
            GPIO.output(ledPin6, False)
            GPIO.output(ledPin7, False)
            GPIO.output(ledPin8, False)
            print("LED OFF")
            sleep(1) #wait for 1 sec
    finally:
     #reset the GPIO Pins
        GPIO.output(ledPin1, False)
        GPIO.output(ledPin2, False)
        GPIO.output(ledPin3, False)
        GPIO.output(ledPin4, False)
        GPIO.output(ledPin5, False)
        GPIO.output(ledPin6, False)
        GPIO.output(ledPin7, False)
        GPIO.output(ledPin8, False)
        GPIO.cleanup()


def fn2():
    try:
        while True:
            GPIO.output(ledPin1, True) #Set the LED Pin to HIGH
            sleep(0.1)
            GPIO.output(ledPin2, True)
            sleep(0.1)
            GPIO.output(ledPin3, True)
            sleep(0.1)
            GPIO.output(ledPin4, True)
            sleep(0.1)
            GPIO.output(ledPin5, True)
            sleep(0.1)
            GPIO.output(ledPin6, True)
            sleep(0.1)
            GPIO.output(ledPin7, True)
            sleep(0.1)
            GPIO.output(ledPin8, True)
            sleep(0.1)
            print("LED ON")
            sleep(0.1) #Wait for 1 sec
            GPIO.output(ledPin8, False) #Set the LED Pin to LOW
            sleep(0.1)
            GPIO.output(ledPin7, False)
            sleep(0.1)
            GPIO.output(ledPin6, False)
            sleep(0.1)
            GPIO.output(ledPin5, False)
            sleep(0.1)
            GPIO.output(ledPin4, False)
            sleep(0.1)
            GPIO.output(ledPin3, False)
            sleep(0.1)
            GPIO.output(ledPin2, False)
            sleep(0.1)
            GPIO.output(ledPin1, False)
            sleep(0.1)
            print("LED OFF")
            
    finally:
     #reset the GPIO Pins
        GPIO.output(ledPin1, False)
        GPIO.output(ledPin2, False)
        GPIO.output(ledPin3, False)
        GPIO.output(ledPin4, False)
        GPIO.output(ledPin5, False)
        GPIO.output(ledPin6, False)
        GPIO.output(ledPin7, False)
        GPIO.output(ledPin8, False)
        GPIO.cleanup()


fn2()
