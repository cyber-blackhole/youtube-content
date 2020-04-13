class Base(object):
    def __init__(self):
        print("In base")


class Derived(Base,object):
    def __init__(self):
        super(Derived,self).__init__()
        print("In derived")

