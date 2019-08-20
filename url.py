import urllib.request
import RPi.GPIO as io
import time
pin1=20
pin2=21
io.setmode(io.BCM)
io.setup(pin1,io.OUT)
io.setup(pin2,io.OUT)

def blink_on(pin0,pin1,delay):
        for x in range(0,10):
            io.output(pin0,True)
            time.sleep(delay);
            io.output(pin0,False)
            io.output(pin1,True)
            time.sleep(delay);
            io.output(pin1,False)
def blink_off(pin0,pin1):
        io.output(pin0,False)
        io.output(pin1,False)

for x in range(0,100):
    req = urllib.request.Request('https://webstartka.000webhostapp.com/rasp/rasp.php?pass=??')
    with urllib.request.urlopen(req) as response:the_page = response.read()
    status=str(the_page)
    print(status)
    if status==str("b'on'"):
        print("led is on")
        blink_on(pin1,pin2,0.1)
    else:
         blink_off(pin1,pin2)
    time.sleep(0.5)
io.cleanup()
    