#Ultrasonic code
from machine import time_pulse_us
import microbit as m
import time

trig = m.pin12
echo = m.pin13
trig.write_digital(1)
echo.read_digital()
start_t = time.ticks_ms()
interval = 40

def detect():
    global start_t
    if (time.ticks_ms() - start_t > interval):
        trig.write_digital(1)
        trig.write_digital(0)
        us = time_pulse_us(echo, 1, 5000)
        if us >= 0:
            t_echo = (us / 1000000)
            dist_cm = (t_echo / 2) * 34300
            return int(dist_cm)
        start_t = time.ticks_ms()
    return None
    