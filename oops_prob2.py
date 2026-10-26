class Account:
    def __init__(self,balance,account_no):
        self.balance=balance
        self.account_no=account_no
    def debit(self,amount):
        self.balance=self.balance-amount
        print(amount,"debited from your account")
    def credit(self,amount):
        self.balance=self.balance+amount
        print(amount,"credited to your account")
    def check_bal(self):
        print(self.balance)    

acc1=Account(10000,1234)
print("Your account number is",acc1.account_no)
print("Your balance is",acc1.balance)
acc1.debit(200)
acc1.credit(1200)
acc1.check_bal()