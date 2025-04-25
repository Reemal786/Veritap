import board #accessing PI's pins
import busio #I2C comm
import adafruit_ds3231 #library for RTC module
import time # getting time from RTC module
from datetime import datetime #allows for easy readable time/data
i2c = busio. I2C (board. SCL, board. SDA) #set up I2C comm using Pi's SDA and SCL 
rtc = adafruit_ds3231.DS3231(i2c) # connecting to RTC using I2C
#year, month, day, hour, minute, second, weekday, yesterday, daylight savings 
rtc.datetime = time.struct_time((2025, 4, 21, 3, 30, 0, 0, -1, -1))
# testing purposes, wont display RTC time, just confirmation
print("RTC has been set to:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
