import lcd_example
import sys, select


d = lcd_example.LCD_1inch14()
d.fill(0)

p = select.poll()
p.register(sys.stdin, select.POLLIN)
while True:
    for  _ in p.ipoll():
            read = sys.stdin.readline()
            if "CPU" in read.upper():
                d.fill_rect(40, 70, 200, 20, 0)
                d.text(read.strip(), 40, 70, 0xFFFF)
                d.show()
            elif "count" in read.lower():
                d.fill_rect(40, 90, 200, 20, 0)
                d.text(read.strip(), 40, 90, 0xFFFF)
                d.show()
            elif "temp" in read.lower():
                val = read.split(':')
                tem = val[1]
                c = tem.split()
                num = float(c[0])
                if num <= 60:
                    d.fill_rect(40, 110, 200, 20, 0)
                    d.text(read.strip(), 40, 110, 0x001f)
                    d.show()
                else:
                    d.fill_rect(40, 110, 200, 20, 0)
                    d.text(read.strip(), 40, 110, 0xf800)
                    d.show()
                     
                     


            
