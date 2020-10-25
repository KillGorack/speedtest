import SpeedTest
import DataPost
import ModemFunctions
import threading
from datetime import datetime

current_hour = datetime.now().hour

while 1:
    if(datetime.now().hour != current_hour):
        s = SpeedTest.SpeedTest()
        results = s.Test()
        d = DataPost.DataPost()
        d.PostToKillGorack(results)
        print("test ran @ " + datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
        current_hour = datetime.now().hour
