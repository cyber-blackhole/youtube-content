#!/usr/bin/python

def printHello(time, *vars):
    print vars
    for v in vars:
        print str(v) +" times "

if __name__=='__main__':
    printHello(1,2,3,4,5,6,7)
