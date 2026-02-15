import serial
import psutil

ser = serial.Serial('/dev/ttyACM0')  
print(ser.name) 

str = b'CPU:' 
str2 = b'count:' 
str3 = b'temp:'
str4 = b'frequency:'


while True:

    load = psutil.cpu_percent(interval=1)
    count = psutil.cpu_count()
    temp = psutil.sensors_temperatures()
    freq = psutil.cpu_freq()
    


    write_cpu  = ('%s %%\n' % load ).encode()
    write_count  = ('%s\n' % count ).encode()
    ser.write(str + write_cpu)
    ser.write(str2 + write_count)


    if 'coretemp' in temp:
        for entry in temp['coretemp']:
            write_temp = ('%s C\n' % entry.current).encode()

    ser.write(str3 + write_temp)


    write_freq = ('%s\n' % round(freq[0], 3)).encode()
    ser.write(str4 + write_freq)


      
ser.close()  