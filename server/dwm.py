import serial
import time

class DWM:
    def __init__(self):
        self._serial_port = None

    def __enter__(self, port='/dev/ttyACM0', baud=115200):
        self._serial_port = serial.Serial(port, baud)
        self._serial_port.write('\r\r'.encode())
        time.sleep(1)
        self._serial_port.write('lec\r'.encode())
        time.sleep(1)
        return self

    def __exit__(self, exc_type, exc_value, tb):
        self._serial_port.write('\r'.encode())
        self._serial_port.close()
        return True

    def locate(self):
        # read the output of the 'lec' command
        try:
            bytes = self._serial_port.readline()
            if bytes:
                cells = bytes.decode().split(',')
                pos_block = cells.index('POS')
                pos_block = cells[pos_block + 1 : pos_block + 4]
                return tuple([float(s) for s in pos_block])
        except Exception as ex:
            return None
        return None

if __name__ == '__main__':
    with DWM() as dwm:
        while True:
            pos = dwm.locate()
            if pos:
                print(pos)