class Person(object):
    def __init__(self,fname,lname):
        print("in person")

    def getName(self):
        print(self.fname,self.lname)

class Student(Person,object):
    def __init__(self,fname,lname):
        print("ins student")

    def getRoll(self):
        print(self.rollno)


