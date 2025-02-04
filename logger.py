import os
import time
import board
import adafruit_dht

dht_device = adafruit_dht.DHT22(board.D19)

try:
    f = open('/home/pi/humidity.csv', 'a+')
    if os.stat('/home/pi/humidity.csv').st_size == 0:
            f.write('Date,Time,Temperature C, Temperature F,Humidity\r\n')
except:
    pass
while True:
    try:
        temperature_c = dht_device.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dht_device.humidity

        f.write('{0},{2:0.1f}*C,{2:0,1f}*F,{3:0.1f}%\r\n'.format(time.strftime('%m/%d/%y'), time.strftime))
    except RuntimeError as err:
        print(err.args[0])
time.sleep(30)