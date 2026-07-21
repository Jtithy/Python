#Author: Tithy
#Date: 2026-07-21
#Description: Create a digital clock that displays the current time.

import datetime
import time

def digital_clock():
    while True:
        #Current Time
        now = datetime.datetime.now()
        print(now.strftime("%H:%M:%S"), end="\r")
        time.sleep(1)

digital_clock()
