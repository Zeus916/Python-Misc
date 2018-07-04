'''
This script eliminates the Carriage return from the barcode reader and returns the raw data in string Format

KeyStrokes for the string so obtained is also genereated.

Configure the scannerto USB RS232 standard.
'''

import serial
import time
from pynput.keyboard import Key, Controller

PORT = input("Enter the COM PORT OF barcode Scanner: ")

SERIAL_PORT = PORT.upper()
SERIAL_RATE = 9600

Byte_list = []

ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)   
print("Keep The Console Minimised Do Not Close")  
        
if __name__ == "__main__":
    while True:
        while True:
            rx_data = ser.read()
            if (rx_data == b'\r'):
                break            
            else:
                Byte_list.append(str(rx_data))
    
        byteAppenedString=''.join(Byte_list)
        dataString  = byteAppenedString.replace('b','').replace("'","")
        print("Barcode Scanned: ", dataString)
  
        key = Controller()
        #time.sleep(5)

        for char in dataString:
            key.press(char)
            key.release(char)
        Byte_list = []
    
    
