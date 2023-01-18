import os
import time

def read_temp():
    temp = os.popen("vcgencmd measure_temp").readline()
    return (temp.replace("temp=","").replace("'C\n",""))

while True:
    print("Temperature: " + read_temp())
    time.sleep(1)
