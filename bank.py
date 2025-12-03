import test
from test import Bank_system
acct = Bank_system()

print("Welcome to the ATM")
while test.validation() == True:
    print("1. withdraw")
    print("2. Check Balance")
    print("3. Buy Airtime")
    print("4. Deposit fund")
    break
choice = int(input("What Do You want to do "))
if choice == 1:
    acct.withdraw()
elif choice == 2:
     acct.balance_check()  
elif choice == 4:
    acct.deposit()
else:
    print("Invalid Response")