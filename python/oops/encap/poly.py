#!/usr/bin/python3

class Flight:
    def fly(self):
        print("flight")

class Jet(Flight):
    def fly(self):
        print("Jet")

class Helicopter(Flight):
    def fly(self):
        print("Helicopter")

def test_fly(ob):
    ob.fly()


f = Flight()
j = Jet()
h = Helicopter()

test_fly(f)
test_fly(j)
test_fly(h)
