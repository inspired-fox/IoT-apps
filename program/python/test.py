# -*- coding: utf-8 -*-
"""
DHT22 RaspberryPi 3 B
温度、湿度センサーのテスト

# Copyright (c) 2020
# Author: TTY

"""

import sys
import Adafruit_DHT
from time import sleep

TEMP_SENSOR_PIN = 4 # 温湿度センサーのピンの番号
INTERVAL = 5 # 監視間隔（秒）
RETRY_TIME = 3 # dht22から値が取得できなかった時のリトライまので秒数
MAX_RETRY = 20 # dht22から温湿度が取得できなかった時の最大リトライ回数

class EnvSensorClass: # 温湿度センサークラス
    def GetTemp(self): # 温湿度を取得
        instance = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, TEMP_SENSOR_PIN)
        #print(instance)
        retry_count = 0
        while True: # MAX_RETRY回まで繰り返す
            retry_count += 1
            result_hum,result_temp = instance
            if result_hum and result_temp != "": # 取得できたら温度と湿度を返す
                return result_temp, result_hum
            elif retry_count >= MAX_RETRY:
                return 99.9, 99.9 # MAX_RETRYを過ぎても取得できなかった時に温湿度99.9を返す
            sleep(RETRY_TIME)
#main
try:
    if __name__ == "__main__":
        env = EnvSensorClass()
        while True:
            temp, hum = env.GetTemp() # 温湿度を取得
            print("temperature = ", temp, " humidity = ", hum, "％")
            sleep(INTERVAL)
except KeyboardInterrupt:
    pass
print('Failed to get reading. Try again!')
sys.exit(1)

