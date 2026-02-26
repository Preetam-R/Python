#create a class consists of 2 attributes 

class Bank:
    def __init__(self,bal,acc):
        self.balance = bal
        self.acc_no = acc

    def debit(self,amount):
        self.balance -= amount
        print(f"Rs.{amount} was debited from your {self.acc_no} Account.")

    def credit(self,amount):
        self.balance += amount
        print(f"Rs.{amount} was Credited to your {self.acc_no} Account.")
    
    def get_balance(self):
        return self.balance
    

acc1 = Bank(1000,12345)

acc1.get_balance()

acc1.credit(500)

print(acc1.get_balance())