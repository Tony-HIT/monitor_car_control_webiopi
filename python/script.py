import webiopi
import time 
import sys

GPIO = webiopi.GPIO

pin7  = 4
pin11 = 17
pin13 = 27
pin15 = 22

# setup function is automatically called at WebIOPi startup
def setup():    
    GPIO.setFunction(pin7,  GPIO.OUT)#all 10 --> 7
    GPIO.setFunction(pin11, GPIO.OUT)
    GPIO.setFunction(pin13, GPIO.OUT)
    GPIO.setFunction(pin15, GPIO.OUT)
    
    GPIO.digitalWrite(pin7,  GPIO.LOW)
    GPIO.digitalWrite(pin11, GPIO.LOW)
    GPIO.digitalWrite(pin13, GPIO.LOW)
    GPIO.digitalWrite(pin15, GPIO.LOW)



# loop function is repeatedly called by WebIOPi 
def loop():
    # gives CPU some time before looping again
    webiopi.sleep(1)



# destroy function is called at WebIOPi shutdown
def destroy():
    GPIO.digitalWrite(pin7,  GPIO.LOW)
    GPIO.digitalWrite(pin11, GPIO.LOW)
    GPIO.digitalWrite(pin13, GPIO.LOW)
    GPIO.digitalWrite(pin15, GPIO.LOW)

@webiopi.macro
def stop():
    GPIO.digitalWrite(pin7,  GPIO.LOW)
    GPIO.digitalWrite(pin11, GPIO.LOW)
    GPIO.digitalWrite(pin13, GPIO.LOW)
    GPIO.digitalWrite(pin15, GPIO.LOW)


@webiopi.macro
def forward(dl):
    GPIO.digitalWrite(pin7,  GPIO.LOW)
    GPIO.digitalWrite(pin11, GPIO.HIGH)
    GPIO.digitalWrite(pin13, GPIO.HIGH)
    GPIO.digitalWrite(pin15, GPIO.LOW)
    time.sleep(dl)
	#replace GPIO.cleanup()
    GPIO.digitalWrite(pin11, GPIO.LOW)
    GPIO.digitalWrite(pin13, GPIO.LOW)


@webiopi.macro
def reverse(dl):
    GPIO.digitalWrite(pin7,  GPIO.HIGH)
    GPIO.digitalWrite(pin11, GPIO.LOW)
    GPIO.digitalWrite(pin13, GPIO.LOW)
    GPIO.digitalWrite(pin15, GPIO.HIGH)
    time.sleep(dl)
	#replace GPIO.cleanup()
    GPIO.digitalWrite(pin7,  GPIO.LOW)
    GPIO.digitalWrite(pin15, GPIO.LOW)


@webiopi.macro
def turn_left(dl):
    GPIO.digitalWrite(pin7,  GPIO.HIGH)
    GPIO.digitalWrite(pin11, GPIO.LOW)
    GPIO.digitalWrite(pin13, GPIO.HIGH)
    GPIO.digitalWrite(pin15, GPIO.LOW)
    time.sleep(dl)
	#replace GPIO.cleanup()
    GPIO.digitalWrite(pin7,  GPIO.LOW)
    GPIO.digitalWrite(pin13, GPIO.LOW)
    

@webiopi.macro
def turn_right(dl):
    GPIO.digitalWrite(pin7,  GPIO.LOW)
    GPIO.digitalWrite(pin11, GPIO.HIGH)
    GPIO.digitalWrite(pin13, GPIO.LOW)
    GPIO.digitalWrite(pin15, GPIO.HIGH)
    time.sleep(dl)
	#replace GPIO.cleanup()
    GPIO.digitalWrite(pin11, GPIO.HIGH)
    GPIO.digitalWrite(pin15, GPIO.LOW)
    

@webiopi.macro
def pivot_left(dl):
    GPIO.digitalWrite(pin7,  GPIO.HIGH)
    GPIO.digitalWrite(pin13, GPIO.HIGH)
    time.sleep(dl)
    GPIO.digitalWrite(pin7,  GPIO.LOW)
    GPIO.digitalWrite(pin13, GPIO.LOW)


@webiopi.macro
def pivot_right(dl):
    GPIO.digitalWrite(pin11, GPIO.HIGH)
    GPIO.digitalWrite(pin15, GPIO.HIGH)
    time.sleep(dl)
	#replace GPIO.cleanup()
    GPIO.digitalWrite(pin11, GPIO.HIGH)
    GPIO.digitalWrite(pin15, GPIO.LOW)
    
    
    

