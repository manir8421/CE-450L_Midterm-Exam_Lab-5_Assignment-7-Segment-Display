
import RPi.GPIO as GPIO
import time


SDI = 17    
RCLK = 27   
SRCLK = 22  


GPIO.setmode(GPIO.BCM)
GPIO.setup([SDI, RCLK, SRCLK], GPIO.OUT)

segment_codes = {
    '0': 0b1000000,  '1': 0b1111001,  '2': 0b0100100,  '3': 0b0110000,
    '4': 0b0011001,  '5': 0b0010010,  '6': 0b0000010,  '7': 0b1111000,
    '8': 0b0000000,  '9': 0b0010000,  'A': 0b0001000,  'B': 0b0000011,
    'C': 0b1000110,  'D': 0b0100001,  'E': 0b0000110,  'F': 0b0001110,
    'G': 0b0010000,  'H': 0b0001001,  'I': 0b1111001,  'J': 0b1110001,
    'K': 0b0001111,  'L': 0b1000111,  'M': 0b1001001,  'N': 0b0101011,
    'O': 0b1000000,  'P': 0b0001100,  'Q': 0b0011000,  'R': 0b0101111,
    'S': 0b0010010,  'T': 0b0000111,  'U': 0b1100011,  'V': 0b1000001,
    'W': 0b1001001,  'X': 0b0001001,  'Y': 0b0010001,  'Z': 0b0100100,
}

def hc595_shift(data):
    GPIO.output(RCLK, GPIO.LOW)
    for bit in range(16):  
        GPIO.output(SRCLK, GPIO.LOW)
        GPIO.output(SDI, (data >> (15 - bit)) & 0x01)
        GPIO.output(SRCLK, GPIO.HIGH)
    GPIO.output(RCLK, GPIO.HIGH)

def display_value(value):
    if isinstance(value, int) and 1 <= value <= 25:
        tens = value // 10
        ones = value % 10
        tens_code = segment_codes[str(tens)] if tens else 0b1111111
        ones_code = segment_codes[str(ones)]
    elif isinstance(value, str) and value.upper() in segment_codes:
        tens_code = 0b1111111
        ones_code = segment_codes[value.upper()]
    else:
        print("Invalid value.")
        return
    
    combined_code = (tens_code << 8) | ones_code
    hc595_shift(combined_code)

try:
    while True:
        # Display numbers 1-25
        for num in range(1, 26):
            display_value(num)
            time.sleep(1)
        
        # Display letters A-Z
        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            display_value(letter)
            time.sleep(1)
except KeyboardInterrupt:
    print("Program stopped by user.")
finally:
    GPIO.cleanup()
    print("GPIO cleaned up.")
