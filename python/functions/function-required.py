#!/usr/bin/python

def printHello(time):
    print "Hello World "+str(time)+" times"


if __name__=='__main__':
    for i in range(1,11):
        printHello(i)
