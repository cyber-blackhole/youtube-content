class Base:
    def __init__(self):
        print("im in base")

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("im in derived")
