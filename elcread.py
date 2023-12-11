"""
Read out electricity meter
"""

import serial
import io
import sys
import iec62056


def main():
    ser = serial.Serial('/dev/ttyUSB0', 9600, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE, timeout=2)
    #ser = serial.Serial('/dev/ttyUSB0', 9600, serial.SEVENBITS, serial.PARITY_EVEN, serial.STOPBITS_ONE, timeout=2)
    #outfile = open('counter.bin', 'wb')

    while True:
        byte = ser.read()
        #strData = response.decode()
        sys.stdout.write(byte.hex()+' ')
        #print(byte)
        #outfile.write(byte
"""        
        p = iec62056.parser.Parser()
        t = p.parse(bytes.decode())
        print(t.keys())
        for k in t.keys():
            o = t[k]
            if isinstance(o, iec62056.objects.Register):
                print('  {} = {}'.format(k, o.value))
"""    
main()
#outfile.close()
