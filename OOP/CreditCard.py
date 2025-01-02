# Base Class / Parent Class / Superclass
class CreditCard:
    
    def __init__(self, customer, bank, acct, limit):
        self._customer = customer
        self._bank = bank
        self._acct = acct
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        return self._customer
    
    def get_bank(self):
        return self._bank   

    def get_account(self):
        return self._acct    

    def get_limit(self):
        return self._limit
    
    def get_balance(self):
        return self._balance

    def charge(self, price):
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        self._balance -= amount

# Inheritance - Child Class / Subclass
class PredatoryCreditCard(CreditCard): # How inheritance is done

    OVERLIMIT_FEE = 5 # Class level member

    def __init__(self, customer, bank, acct, limit, apr): # Creating a new instance of predatoryCredit card
        super().__init__(customer, bank, acct, limit) # Calling super constructor using super() --> the one in base class
        self._apr = apr

    def charge(self, price):
        success = super().charge(price)
        if not success:
            self._balance += PredatoryCreditCard.OVERLIMIT_FEE
        return success
    
    def process_month(self):
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor

    