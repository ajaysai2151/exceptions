class BankAccount: #usbalemodeleDeveloper
    def __init__(self,account_number):
        self.account_number = str(account_number)
        self.balance = 0 
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount 
        else:
            raise ValueError("Insufficient Funds")
            #print("Insufficient Funds")
    def deposit(self,amount):
        self.balance += amount 
    def get_balance(self):
        return(self.balance)
def transfer_amount(account_1,account_2,amount): #endapplicationDeveloper
    try:
        account_1.withdraw(amount)
        account_2.deposit(amount)
        return "Sucessful"
        
    except ValueError as e:
        #raise chysi dani pakana ah exception class peytamo adi echi aliqsing evalli 
        #exception raise inapudu e block execute avutadi apudu object create avutadi
        #raise ValueError("Insufficient Funds")
        #raise ani chypi accpetions class use chysi acception ni raise chysamu
        #value error aneydi class kabbati edi object return chystadi 
        #so manam ah object ni acces chyachu  
        print(str(e)) #classes lopala raisna arguments vastai 
        print(type(e)) #ah class use chysamo adi vastadi 
        print(e.args) #manam class ki pampina argumnets tuple laga vastai
        return "Failed"
user_1 = BankAccount("001")
user_2 = BankAccount("002")
user_1.deposit(25)
user_2.deposit(100)

print("user 1 balance {}/-".format(user_1.get_balance()))
print("user 2 balance {}/-".format(user_2.get_balance()))
print(transfer_amount(user_1,user_2,50))
print("transfering 50/- from user_1 to user_2")
print("user 1 balance {}/-".format(user_1.get_balance()))
print("user 2 balance {}/-".format(user_2.get_balance()))











