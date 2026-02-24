class gautam_bank():
    ifsc_code = "SBI00332"
    branch_loc = "Bangalore"
    roi=0.07

    def __init__(self, name, accno, bln, phno,pin):
        self.name = name
        self.accno = accno
        self.bln = bln
        self.phno = phno
        self.pin=pin
        
    def details(self):
        print(f"Name               ={self.name}")
        print(f"account numner     ={self.accno}")
        print(f"phone number       ={self.phno}")
    def withdraw(self):
        attempts=3
        while attempts>0:
            if gautam_bank.getpassword()==self.pin:
                    
                w_amount = int(input("Enter the withdrawal amount: "))
                if w_amount <= self.bln:
                    if w_amount % 100 == 0:
                        if 500 <= w_amount <= 15000:
                            self.bln -= w_amount
                            print("Transaction successful, amount deducted.")
                            print(f"Available balance: {self.bln}")
                            break
                        else:
                            print("Enter a valid amount.")
                    else:
                        print("Invalid denomination.")
                else:
                    print("Insufficient balance.")
            else:
                print("invalid password")
                attempts-=1
                print(f"the number of attempts left{attempts}")
        else:
            print("the account is blocked for 24 hours")
    def deposit(self):
        if self.accno == int(input("Enter the account number: ")):
            d_amount = int(input("Enter the amount: "))
            if d_amount % 100 == 0:
                if 100 <= d_amount <= 50000:
                    self.bln += d_amount
                    print(f"Balance credited. Credited amount: {d_amount}")
                    print(f"Available balance: {self.bln}")
                else:
                    print("Enter a valid amount.")
            else:
                print("Invalid denomination.")
    def checkbalance(self):
        attempts=3
        while attempts>0:
            if gautam_bank.getpassword()==self.pin:
                print(f"the currrent balance is {self.bln}")
                break
            else:
                print("invalid password")
                attempts-=1
                print(f"the number of attempts left{attempts}")
        else:
            print("block for 24 hours")
    @staticmethod
    def getpassword():
        password=int(input("enter the password: "))
        return password
    
cust1 = gautam_bank("gautam", 933452456878, 30000, 7606935231,1111)
cust2 = gautam_bank("pritam", 933452456874, 20000, 9080854047,3333)
cust3 = gautam_bank("sritam", 933452456873, 10000, 6370706629,2222)
cust4=gautam_bank("ganesh", 933452456873, 10000000, 6370706625,4444)
cust4.withdraw()
# cust4.deposit()

# print(cust1.checkbalance())

