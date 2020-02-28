import RPi.GPIO as GPIO
import time
import serial

def read_rfid ():
    ser = serial.Serial ("/dev/ttyUSB0") #Open named port
    ser.baudrate = 9600 #Set baud rate to 9600
    data = ser.read(13) #Read 12 characters from serial port to data
    ser.close () #Close port
    return data #Return data
try:
    while True:
        id = read_rfid ()
        print (id) #Print RFID
        idcheck="40003515A5C54"
        print(idcheck)
        if id==idcheck: #replace the ID number with your ID number
            print("Acces Granted")
        else:
            print("Access Denied")

finally:
    GPIO.cleanup()