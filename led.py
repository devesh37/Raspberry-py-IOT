import RPi.GPIO as io
import time as time
pin1=21
pin2=20
io.setmode(io.BCM)
io.setup(pin1,io.OUT)
io.setup(pin2,io.OUT)
for x in range(0,10):
    time.sleep(1)
    io.output(pin1,True)
    io.output(pin2,True)
    time.sleep(1)
    io.output(pin1,False)
    
io.output(pin2,False)
    
io.cleanup()
