import RPi.GPIO as GPIO
import time

SER = 17  
RCLK = 27  
SRCLK = 22 

GPIO.setmode(GPIO.BCM)
GPIO.setup(SER, GPIO.OUT)
GPIO.setup(RCLK, GPIO.OUT)
GPIO.setup(SRCLK, GPIO.OUT)

segment_values = {
    '0': 0b0111111,
    '1': 0b0000110,
    '2': 0b1011011,
    '3': 0b1001111,
    '4': 0b1100110,
    '5': 0b1101101,
    '6': 0b1111101,
    '7': 0b0000111,
    '8': 0b1111111,
    '9': 0b1101111,
    'A': 0b1110111,
    'b': 0b1111100,
    'c': 0b1011000,
    'd': 0b1011110,
    'E': 0b1111001,
    'F': 0b1110001,
}

def shiftOut(byte):
    GPIO.output(RCLK, 0)  
    for bit in range(8):
        GPIO.output(SER, 0 if byte & (1 << (7 - bit)) else 1)
        GPIO.output(SRCLK, 1) 
        time.sleep(0.00001) 
        GPIO.output(SRCLK, 0)
    GPIO.output(RCLK, 1) 

try:
    characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    while True:
        for char in characters:
            shiftOut(segment_values[char])
            time.sleep(1)

finally:
    shiftOut(0b0000000) 
    GPIO.cleanup() 
