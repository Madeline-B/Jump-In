import RPi.GPIO as GPIO
from time import sleep, time
import random
 
DEBUG = False
SETTLE_TIME = 2
CALIBRATIONS = 5      #how many calibrations will i check
CALIBRATION_DELAY = 2 #how much between calibrations
TRIGGER_TIME = 0.0001
SPEED_OF_SOUND = 343 # 343 m/s
known_distance = 35
difficulty = 0.75
 
GPIO.setmode(GPIO.BCM)
TRIG = 18
ECHO = 27
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
 
def getDistance():
    #activate the trigger
    GPIO.output(TRIG, GPIO.HIGH)
    sleep(TRIGGER_TIME)
    GPIO.output(TRIG, GPIO.LOW)
    
    while (GPIO.input(ECHO) == GPIO.LOW):
        start = time()
    while (GPIO.input(ECHO) == GPIO.HIGH):
        stop = time()
    # now that we have the time, convert it to distance in cm
    duration = stop-start
    distance = duration * SPEED_OF_SOUND
    distance /= 2 #divide the stance by 2
    distance *= 100 # change to cm
    
    return distance
 
def calibrate():
    print ("Calibrating.....")
    #ask the user to place my control measurment
    print ("-Place the sensor a measured distance away from an object")
    known_distance = 35
    distance_avg = 0
    
    # take a few known measurements and get the sum
    for i in range(CALIBRATIONS):
        distance = getDistance()
        distance_avg += distance
        sleep(CALIBRATION_DELAY)
        
    # then change it to an average
    distance_avg /= CALIBRATIONS
    
    if(DEBUG):
        print("--Average is {} cm".format(distance_avg))
    
    correction_factor = known_distance / distance_avg
    
    if(DEBUG):
        print("--Correction Factor is {}.".format(correction_factor))
    
    print ("Done\n")
    return correction_factor
 
def jump():
    correction_factor = calibrate()
    distance = getDistance()
    if distance < (known_distance - correction_factor):
        reStart()
        return "nay"
    else:
        sleep (difficulty)
        return "yay"
    
 
def reStart():
    again = input("\nPress enter to go again ")
    if again == " " or "":
        Main()


def Main():
    print("Initializing...")
    calibrate()
    print("Done with calibration")
    counter = 0
    print("Begin Jumping")
    jump()
    while True:
        if jump == "yay":
            jump()
            counter =+ 1
            print("yay, you jumped the rope.")
        else:
            break
    print("you got to {} jumps! Good Job!").format(counter)
    reStart()
Main()
