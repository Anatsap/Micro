import lcd_example
from machine import UART, Pin
import time


d = lcd_example.LCD_1inch14()
d.fill(0)


uart = UART(1, baudrate=115200, tx=Pin(4), rx=Pin(5))


while True:
    uart.write("Hello from MicroPython!\n")
    
    if uart.any():
        read_m = uart.read()
        if read_m:
            decoded = read_m.decode('utf-8')
            d.fill_rect(40, 70, 180, 40, 0)       
            d.text(decoded.strip(), 40, 70, 0xFFFF)
            
            uart.write(decoded)
            d.show()        
    time.sleep(1)



            
