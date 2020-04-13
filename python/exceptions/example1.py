#!/usr/bin/python


print("before division")
try:
    print(1/0)
except ZeroDivisionError:
    print("handled zero division")
print("after division")
