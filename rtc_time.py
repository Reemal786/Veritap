# accessing PI's pins
import board
import busio #allows I2C comm
import adafruit_ds3231 #Library for RTC module
from RPLCD.i2c import CharLCD #LCD library for I2C comm 
from time import sleep #time
from datetime import datetime #date
# set up I2C comm using Pi's SDA and SCL
i2c = busio.I2C (board. SCL, board.SDA)
# connecting to RTC module using I2C 
rtc = adafruit_ds3231.DS3231 (i2c)
#comm between pi and LCD
lcd = CharLCD('PCF8574', 0x27)
# Read time from RTC
raw_time = rtc.datetime

now = datetime (*raw_time [:6]) # takes first six values from RTC 
time_str = now.strftime("%H:%M:%S") #converts to time format 
date_str = now.strftime("%m/%d/%Y") #converts to data format
# Display on LCD
lcd.clear() #clears LCD
lcd.write_string(time_str) #prints time on first line 
lcd.cursor_pos = (1, 0) # Move to second line
lcd.write_string(date_str) #prints date on second line

sleep (5) #displays for 5 secs
lcd.clear() #clears after 5 secs
