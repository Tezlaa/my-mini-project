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

ser = serial.Serial(
    port=result[0],
    baudrate=s.baudrate,
    bytesize=s.bytesize,
    parity=s.parity,
    stopbits=s.stopbits,
    timeout=0.05)

print(ser.readline())

time.sleep(4)

# ser.write("AT+CMGL=\"ALL\"\r\n".encode("utf-8"))

# while True:
#     gelen = str(ser.readline().decode("UTF-8", errors='replace'))

#     gelen = gelen.replace('\r', '').replace('\n', '')
#     if len(gelen) > 0:
#         print(gelen)

