class Person(object):
    def __init__(self,name,address):
        self.name=name
        self.address=address
        print("In Person")

    def get_name(self):
        return self.name

    def sayHello(self):
        print("Im from Person")


class BankCustomer(Person,object):
    def __init__(self,accountNumber,name,address):
        super(BankCustomer,self).__init__(name,address)
        self.accountNumber=accountNumber
        print("In BankCustomer")

    def get_accountNumber(self):
        return self.accountNumber

    def sayHello(self):
        super().sayHello()
        print("Im BacnkCustomer")

#d = BankCustomer(928367362,"cyber blackhole","chennai")
