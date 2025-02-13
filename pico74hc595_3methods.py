
from machine import Pin
import random
import time

#define PINs according to cabling to the Pico
dataPIN = 13
latchPIN = 15
clockPIN = 14
resetPIN = 16

#set pins to output PIN objects
dataPIN=Pin(dataPIN, Pin.OUT)
latchPIN=Pin(latchPIN, Pin.OUT)
clockPIN=Pin(clockPIN, Pin.OUT)
resetPIN=Pin(resetPIN, Pin.OUT)

#define shift register update function
def shift_out(data, clock, value):
    for i in range(8):
        bit = (value >> (7 - i)) & 0x01
        data.value(bit)
        pulse(clockPIN)

def pulse(pin):
    pin.value(1)
    time.sleep_us(1)
    pin.value(0)
    time.sleep_us(1)
    
#main program, calling shift register function


#Method 1 -Very ugly, but it works 2025-02-12

resetPIN.value(1)
x = 0
lastnum = 0
for i in range(1,17):
    #print(i)
    x = x + 1
    if x < 9:
        ov = [(i-1)//8]
        if x == 1:
            ov.append(1)
            lastnum = 2
        else:    
            lastnum = 2 * lastnum
            ov.append(lastnum - 1)
    else:
        if x == 9:
            rs = lastnum - 1
            ov = [1,rs]
            lastnum = 2
        else:
            lastnum = 2 * lastnum
            ov = [lastnum -1,rs]
    
    print(ov)
    for value in ov:
        shift_out(dataPIN, clockPIN, value)
        
    pulse(latchPIN)
    time.sleep(1.0)

resetPIN.value(0)
pulse(latchPIN)
resetPIN.value(1)
time.sleep(3)

#Method 2 - Wordy, but easily expandible to 3+ registers

for i in range(1,17):            
    if i == 1:
        output_values = [0,1]
    if i == 2:
        output_values = [0,3]
    if i == 3:
        output_values = [0,7] 
    if i == 4:
        output_values = [0,15] 
    if i == 5:
        output_values = [0,31]
    if i == 6:
        output_values = [0,63]
    if i == 7:
        output_values = [0,127]
    if i == 8:
        output_values = [0,255]
    if i == 9:
        output_values = [1,255]
    if i == 10:
        output_values = [3,255]
    if i == 11:
        output_values = [7,255]
    if i == 12: 
        output_values = [15,255]
    if i == 13:
        output_values = [31,255]
    if i == 14:
        output_values = [63,255]
    if i == 15:
        output_values = [127,255]
    if i == 16:
        output_values = [255, 255]       
    print(output_values)
    
    for value in output_values:
        shift_out(dataPIN, clockPIN, value)    
    pulse(latchPIN)
    time.sleep(1.0)
    
time.sleep(3)
resetPIN.value(0)
pulse(latchPIN)
resetPIN.value(1)

#Method 3 - Microsoft CoPilot generated code

output_values = [0x00, 0x00]  # Two shift registers, initial values
for i in range(16):  # 16 outputs in total
    if i < 8:
        output_values[1] |= (1 << i) #change this to output_values[0] if you want to count down
    else:
        output_values[0] |= (1 << (i - 8))  ##change this to output_values[1] if you want to count down
    print(output_values)
    
    for value in output_values:
        shift_out(dataPIN, clockPIN, value)
    pulse(latchPIN)
    
    time.sleep(1)  # Adjust the delay for your needs

time.sleep(1)  # Wait for a second before resetting

resetPIN.value(0)
pulse(latchPIN)