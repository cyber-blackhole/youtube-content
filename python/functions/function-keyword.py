#!/usr/bin/python

def printHello(time, msg):
    print str(time) +" times " + msg


if __name__=='__main__':
    for i in range(1,11):
        printHello("helloworld", i)
