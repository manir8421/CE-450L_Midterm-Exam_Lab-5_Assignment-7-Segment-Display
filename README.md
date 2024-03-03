            
 San Francisco Bay University

CE450 Fundamentals of Embedded Engineering
Lab 5 Driving 7-Segments LEDs

Objectives:
In this lab, the display for some numbers and alphabets will be designed by using several 7-segments LEDs on the Raspberry Pi board through Python program and do hands-on exercise through lab assignments

Introduction:
Two 7-segments LEDs are available in Sunfounder accessory box. The control circuit has been shown using 74HC595(8-bit shift registers) to drive only one 7-segments LED in the following schematic. Three control signals generated from three pins in GPIO port are shifted into 74HC595.
 
Equipment: 
The equipment you require is as follows:
•	Laptop & Raspberry Pi 3 model Board
•	SunFounder Super Starter Kit V2.0 for Raspberry Pi 

The Laboratory Procedure: 
1.	Hardware connection 

 
 

2.	Control program in Python

# Python program
import RPi.GPIO as GPIO
import time

SDI   = 11
RCLK  = 12
SRCLK = 13

segCode = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f,0x77,0x7c,0x39,0x5e,0x79,0x71,0x80]

def print_msg():
	print 'Program is running...'
	print 'Please press Ctrl+C to end the program...'

def setup():
	GPIO.setmode(GPIO.BOARD)    #Number GPIOs by its physical location
	GPIO.setup(SDI, GPIO.OUT)
	GPIO.setup(RCLK, GPIO.OUT)
	GPIO.setup(SRCLK, GPIO.OUT)
	GPIO.output(SDI, GPIO.LOW)
	GPIO.output(RCLK, GPIO.LOW)
	GPIO.output(SRCLK, GPIO.LOW)

def hc595_shift(dat):
	for bit in range(0, 8):	
		GPIO.output(SDI, 0x80 & (dat << bit))
		GPIO.output(SRCLK, GPIO.HIGH)
		time.sleep(0.001)
		GPIO.output(SRCLK, GPIO.LOW)
	GPIO.output(RCLK, GPIO.HIGH)
	time.sleep(0.001)
	GPIO.output(RCLK, GPIO.LOW)

def loop():
	while True:
		for i in range(0, len(segCode)):
			hc595_shift(segCode[i])
			time.sleep(0.5)

def destroy():   #When program ending, the function is executed. 
	GPIO.cleanup()


print_msg()
setup() 
try:
	loop()  
except KeyboardInterrupt:  
	destroy() 

------------------------------------------------------------------------------------------
segCode = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f,0x77,0x7c,0x39,0x5e,0x79,0x71,0x80]

hgfe_dcba
0011_1111 => 0
0000_0110 => 1
... ...
0110_1111 (0x6f)=> 9
0111_0111 (0x77)=> A
0111_1100 (0x7C)=> b
	 (0x5A)=> c
 	 (0x5E)=> d
	 (0x79)=> e
	 (0x71)=> f
... ...	 (0x6F)=> g
	 (0x74)=> h
 	 (0x10)=> i
	 (0x0E)=> j
	 (0x70)=> k
 	 (0x18)=> l
	 (0x49)=> m
    	 (0x54)=> n
	 (0x5C)=> o
... ...	 (0x73)=> p
	 (0x67)=> q
	 (0x50)=> r
	 (0x6D)=> s
	 (0x78)=> t
	 (0x1C)=> u
	 (0x62)=> v
	 (0x36)=> w
	 (0x52)=> x
	 (0x72)=> y
	 (0x43)=> z
1000_0000 (0x80)=> switch-off
	*Note: Hardware connection reference and running command
https://learn.sunfounder.com/lesson-14-driving-7-segment-display-by-74hc595/
	https://learn.sunfounder.com/category/super-kit-v3-0-for-raspberry-pi/

The Laboratory Assignments: 

1.	Implement the 7-segment LEDs control based on the above example program.

2.	Add one more 7-segment LED to the above design for the continuous display of the decimal number from 1 to 25 and alphabet from A-Z display, such as the following.
 
