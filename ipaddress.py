import os
import time
import Adafruit_CharLCD as LCD
import commands


def initialize()
	initialReading = commands.getoutput('hostname -I')
	lcd = LCD.Adafruit_CharLCDPlate()
	print 'Press Ctrl-C to quit.'
	lcd.set_color(1.0, 0.0, 0.0)
	lcd.clear()
	lcd.show_cursor(False)
	lcd.blink(False)
	lcd.clear()
	lcd.message('Local IP Address:\n')
	lcd.message("Finding...")
	time.sleep(3.0)
	return initialReading


def update(reading):
    print("update() triggered")
    if commands.getoutput('hostname -I') == reading:
        print("if statement triggered")
        time.sleep(3.0)
        update(reading)
    else:
        print("else statement triggered")
        newReading = commands.getoutput('hostname -I')
        lcd.clear()
        lcd.message('Local IP Address:\n')
        lcd.message(newReading)
        time.sleep(3.0)
        update(newReading)   

   
def Main():
	initialReading = initialize()
	update(initialReading)

lcd.clear()
