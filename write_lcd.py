# LCD library for I2C communication
from RPLCD.12c import CharLCD
#sleep library used to pause between messages or after
from time import sleep
#allow for passing texts for LCD screen
import sys
lcd = CharLCD('PCF8574', 0x27) #comm btwen pi and LCD
message = sys.argv[1] if len(sys.argv) > 1 else "This Is Veritap" #if not message is passed, then This Is Veritap will be displayed
lcd.clear() #clear LCD
lcd.write_string (message) #display messaged passed
sleep (5) #display message for 5 seconds
lcd.clear() #clear the screen after that
