#Ultrasonic code
from machine import time_pulse_us
import microbit as m

trig = m.pin12
echo = m.pin13

trig.write_digital(0)
echo.read_digital()

while True:
    trig.write_digital(1)
    trig.write_digital(0)
    us = time_pulse_us(echo, 1)
    if us == (-1) or us == (-2):
        print(us)
        print('timeout')
        trig.write_digital(0)
        echo.read_digital()
        m.sleep(1000)
    else:
        t_echo = (us / 1000000)
        dist_cm = (t_echo / 2) * 34300
        print(int(dist_cm))
    m.sleep(100)