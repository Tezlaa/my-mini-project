import time
import sys

from datetime import datetime
from gsmmodem.modem import GsmModem, Sms

import serial.tools.list_ports
import logging


class Gsm:
    def __init__(sefl):
        pass

    def connect_gsm(self, connect: list, pin: int = None) -> None:

        try:
            s = serial.Serial(connect)
            s.close()
        except (OSError, serial.SerialException):
            return "Error"
        print(s)

        PORT = s.port
        BAUDRATE = s.baudrate
        PIN = pin

        #    Uncomment the following line to see what the modem is doing:
        logging.basicConfig(
            format='%(levelname)s: %(message)s', level=logging.DEBUG)

        modem = GsmModem(
            PORT, BAUDRATE, smsReceivedCallbackFunc=self.handle_sms)

        modem.smsTextMode = False
        modem.connect(PIN)

        time.sleep(4)

    def check(self) -> None:

        smss = modem.listStoredSms(status=Sms.STATUS_ALL, delete=True)
        print(str(len(smss)) + ' messages found')

        for i in range(len(smss)):
            sms = smss[i]
            handleSms(sms)

        print('Waiting for new SMS message...')
        try:
            modem.rxThread.join(2**31)
        finally:
            modem.close()

    def close(sefl) -> None:
        modem.close()

    def get_all_connect(self) -> list:

        list_with_connect = serial.tools.list_ports.comports()

        connected = []
        for element in list_with_connect:
            connected.append(element.device)

        return connected

    @staticmethod
    def handle_sms(sms) -> str:
        return f'== SMS message received ==\nFrom: {0}\nTime: {1}\nMessage:\n{2}\n'.format(sms.number, sms.time, sms.text)

    # # if sys.platform.startswith('win'):

    # #     ports = ['COM%s' % (i + 1) for i in range(256)]
    # # elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):

    # #     ports = glob.glob('/dev/tty[A-Za-z]*')
    # # elif sys.platform.startswith('darwin'):

    # #     ports = glob.glob('/dev/tty.*')
    # # else:
    # #     raise EnvironmentError('Unsupported platform')

    # index_with_connect = 0
    # try:
    #     PORT = str(result[index_with_connect])
    #     BAUDRATE = s.baudrate
    #     PIN = None
    # except IndexError:
    #     index_with_connect += 1
