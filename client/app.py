import requests
from dwm import DWM
from python_tsl2591 import tsl2591
import time

ENDPOINT = 'http://192.168.1.124:5000/api/add_message/'

def run_app():
    tsl = tsl2591()
    tsl.enable()
    with DWM() as dwm:
        old_time = time.time() - 1.0
        enabled = False
        while True:
            pos = dwm.locate()
            if pos:
                epoch_time = time.time()
                lux = {}
                # polling quickly is important for the UWB module to 
                # locate, but the lux sensor can't poll too fast.
                if epoch_time - old_time > 1.0:
                    if enabled:
                        lux = tsl.get_current()
                        enabled = False
                    else:
                        tsl.enable()
                        enabled = True
                    wait_time = time.time()
                json = {'location': pos, 'lux': lux, 'epoch_time': epoch_time}
                res = requests.post(ENDPOINT, json=json)

if __name__ == '__main__':
    run_app()
