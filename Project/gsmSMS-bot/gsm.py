from __future__ import print_function
from datetime import datetime
from gsmmodem.modem import GsmModem, Sms

import logging

import serial.tools.list_ports
import time
import sys


list = serial.tools.list_ports.comports()
connected = []
for element in list:
    connected.append(element.device)
print("Connected COM ports: " + str(connected))


if sys.platform.startswith('win'):

    ports = ['COM%s' % (i + 1) for i in range(256)]
elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):

    ports = glob.glob('/dev/tty[A-Za-z]*')
elif sys.platform.startswith('darwin'):

    ports = glob.glob('/dev/tty.*')
else:
    raise EnvironmentError('Unsupported platform')

result = []
for port in ports:
    try:
        s = serial.Serial(port)
        s.close()
        result.append(port)
    except (OSError, serial.SerialException):
        pass
print("Availible COM Ports: " + str(result))

PORT = str(result[0])
BAUDRATE = s.baudrate
PIN = None

def handle_sms(sms):
    print(u'== SMS message received ==\nFrom: {0}\nTime: {1}\nMessage:\n{2}\n'.format(sms.number, sms.time, sms.text))

def main():
    print('Initializing modem...')

    # Uncomment the following line to see what the modem is doing:
    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
    modem = GsmModem(PORT, BAUDRATE, smsReceivedCallbackFunc=handle_sms)
    modem.smsTextMode = False
    modem.connect(PIN)

    #modem.processStoredSms(False)
    smss = modem.listStoredSms(status=Sms.STATUS_ALL, delete=True);
    print(str(len(smss)) + ' messages found')

    for i in range(len(smss)):
        sms = smss[i]
        handleSms(sms)

    print('Waiting for new SMS message...')    
    try:    
        modem.rxThread.join(2**31)
    finally:
        modem.close();

if __name__ == '__main__':
    main()

    input()