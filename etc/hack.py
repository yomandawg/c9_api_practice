# Hacking a GET method
import requests
from time import sleep
url = ""
title = "Don't use"
content = "GET for DB"
url = f'http://{url}/create/?title={title}&content={content}'

while True:
    sleep(5) # 5초마다 DB get
    requests.get(url)