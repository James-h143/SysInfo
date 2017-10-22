import os
import time
import Adafruit_CharLCD as LCD
import commands

#!Global
currentDisp2 = ""


def initialize(lcd):
	initialReading = commands.getoutput('hostname -I')
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


def update(lcd,reading):
	print("update() triggered")
	newReading = commands.getoutput('hostname -I')
	print("hostname is "+newReading)
	def checkNeed(lcd,reading):
			global currentDisp2 
			if currentDisp2 == newReading:
				print("currentDisp2 == reading is true")
				time.sleep(3.0)
				update(lcd,reading)
			else:
				print("currentDisp2 == reading is false")
				lcd.clear()
				lcd.message('Local IP Address:\n')
				lcd.message(newReading)
				time.sleep(3.0)
				currentDisp2 = reading
				update(lcd,newReading)
	if newReading.find(".", 0, len(newReading))!=-1:
		print('newReading.find(".", 0, len(reading))!=-1 is true')
		currentDisp2 = newReading
		checkNeed(lcd,reading)
	else:
		print('newReading.find(".", 0, len(reading))!=-1 is false')
		time.sleep(3.0)
		update(lcd,reading)  

   
def Main():
	lcd = LCD.Adafruit_CharLCDPlate()
	initialReading = initialize(lcd)
	update(lcd,initialReading)
	lcd.clear()
Main()


