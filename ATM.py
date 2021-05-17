# Creating a class for ATM

class ATM(object):

    def __init__(self, atm_card_number,  pin_number):
        self.atmCardNumber = atm_card_number
        self.pin = pin_number
        self.cash = 5000

    def balanceEnquiry(self):
        print("Your Account Balance is", self.cash)

    def cashWithDrawl(self):
        a = int(input("How much Cash you want to withdraw: "))
        self.cash -= a
        print("Successfully Withdrawed")
        print("Remaning balance: ", self.cash)


dhairya = ATM(12345, 1133)
a = 3

while a > 0:
    f = str(input("What do you want to do? Check Balance or Withdraw Cash: "))
    if(f == "check balance"):
        dhairya.balanceEnquiry()
    elif(f == "withdraw cash"):
        dhairya.cashWithDrawl()
    else:
        print("That action is not possible!!")
