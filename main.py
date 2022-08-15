import time

import BME280
from machine import Pin, I2C

from config import room
from deep_sleep import deep_sleep
from send import send_message_to_queue

i2c = I2C(scl=Pin(5), sda=Pin(4))

bme = BME280.BME280(i2c=i2c)  # addr 118


tmp = bme.temperature[:-1]

print(time.time())
message = {"Temp": "{}".format(tmp), "Room": "{}".format(room)}
send_message_to_queue(message)

deep_sleep(10000)
