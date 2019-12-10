import requests, bs4, re, webbrowser

url = 'https://www.googleapis.com/youtube/v3/videos?id=7lCDEYXw3mM&key=AIzaSyAu9SoqdklXCN3Fs-CVZoa1ltipAsrUzTE&part=snippet,contentDetails,statistics,status'

res = requests.get(url)
res.raise_for_status()
print(res.text)
