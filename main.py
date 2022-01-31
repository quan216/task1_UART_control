###

import serial
import time


#######################################################################################

class SystemInitial:  # set up chung port vao day

    def __init__(self, COM1, Baud_rate):
        self.port = COM1
        self.BauRate = Baud_rate
        self.ser = serial.Serial(self.port, self.BauRate, bytesize=8, timeout=0.1)
        self.Tx_data = None

    def send_(self, data1):
        self.Tx_data = data1

        if self.Tx_data == ' ':
            print('receive data from MCU')
            time.sleep(0.5)
            self.ser.write(b' ')

            while True:
                Rx_data = self.ser.read_all()
                for text in Rx_data:
                    print('char: {}, hex: {}, dec: {}'.format(chr(text), hex(text), text))
                    time.sleep(0.5)

        else:
            print('send data to MCU')
            time.sleep(0.5)
            i = 0

            while i < len(self.Tx_data):
                for text in self.Tx_data:
                    i += 1
                    self.ser.write(text.encode('utf-8'))
                    time.sleep(0.1)
                    # send 'data' from PC to MCU

                    print(self.ser.read_all().decode())
                    time.sleep(0.5)


##################################################################################################

COM = "COM6"
BaudRate = {'1': int(115200), '2': int(9600)}
Program = SystemInitial(COM, BaudRate['1'])

while True:
    q = input('send data (Y) or (N) to receive data only: ').upper()
    if q == 'N':
        Program.send_(' ')

    if q == 'Y':
        data = input('input data to send: \n')
        if data == '':
            print('program end')
            time.sleep(0.1)
            break

        else:
            Program.send_(data)
        continue

    else:
        print('program end')
        time.sleep(0.1)
        break
