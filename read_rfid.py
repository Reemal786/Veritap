#library import
#this helps us read from the RFID scanner
from mfrc522 import SimpleMFRC522
#GPIO (gen purpose input/output) library
import RPi.GPIO as GPIO
#assigns the RFID scanner to variable reader
reader = SimpleMFRC522()

try: #reads the card and assigns the ID to variable id
  id = reader.read_id()
  print("Card detected!") #if the card is accepted it will print this statement print(id) 
  print(id) # the associated id number will be printed
#when something goes wrong
except Exception as error: #exception is the default type of error
#sets the error to variable name error
  print("Error:", error) #print this statement
finally:
  GPIO.cleanup()
