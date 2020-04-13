class CustomerClass:
    """Class Documentation"""

    firstname="Cyber"
    lastname="BlackHole"
    account_balance=0

    def __init__(self,fn,ln,bal):
        self.firstname=fn
        self.lastname=ln
        self.account_balance=bal

    def getFirstName(self):
        return self.firstname

    def getLastName(self):
        return self.lastname


