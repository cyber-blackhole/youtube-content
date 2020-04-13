class Person(object):
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def getName(self):
        print(self.fname,self.lname)

class Student(Person,object):
    def __init__(self,rollno,fname,lname):
        Person.__init__(self,fname,lname)
        self.rollno=rollno

    def getRoll(self):
        print(self.rollno)

    def getName(self):
        print(self.fname)
