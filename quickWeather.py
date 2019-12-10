#!/usr/bin/python3
# quickWeather.py - コマンドラインに指定した地名の天気予報を表示する

import json, requests, sys

# コマンドライン引数から地名を組み立てる。
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])

# openweathermap.orgから取得したAPIキーを定義しておく
APPID = '01234567890123456789012345678901'

# OpenWeatherMap.orgのAPIからJSONデータをダウンロードする
url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q={}&cnt=3&appid={}'.format(location, APPID)
response = requests.get(url)
response.raise_for_status()

weather_data = json.loads(response.text)

w = weather_data['list']
print('{}の現在の天気:'.format(location))
print(w[0]['weather'][0])
print()
print()
print()
print()
print()
print()
