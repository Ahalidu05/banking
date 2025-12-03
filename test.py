
def validation():
    card = input("Please insert your card ---")
    if len(card) != 16 or not card.isdigit():
        print("Invalid input. Please enter a 16-digit number.")
    else:
    # Reverse the number and convert to list of ints
        reversed_digits = [int(n) for n in card[::-1]]

    # Apply henry algorithm
    for i in range(len(reversed_digits)):
        if (i + 1) % 2 == 0:
            reversed_digits[i] *= 2
            if reversed_digits[i] > 9:
                reversed_digits[i] -= 9

    total = sum(reversed_digits)


    # Check divisibility
    if total % 10 == 0:
       return True
    else:
        print("Invalid Card Number***")


class Bank_system():
    def __init__(self):
        self.balance = 1000

    def deposit(self):
        confirm_deposit = input('Do you want to deposit? yes/no \n')
        if (confirm_deposit == 'yes'):
            deposit_amount = eval(input('How much do you want to deposit? \n'))
            self.balance =self.balance + deposit_amount
            print('deposit was successful. New amount is {}'.format(self.balance))
    
    def withdraw(self):
        confirm_withdraw = input('Do you want to withdraw? yes /no \n')
        if (confirm_withdraw == 'yes'):
            withdraw_amount = eval(input('How much do you want to withdraw? \n'))
            if (withdraw_amount > self.balance):
                confirm_overdraft = input('You do not have sufficient balance to complete this transaction. \n would you want to request an overdraft? yes/no \n')
                if (confirm_overdraft == 'yes'):
                    print('your request is being reviewed and an email will be sent soon')

            else:
                self.balance -= withdraw_amount
                print('withdraw successful. Your new balance is {}'.format(self.balance))



    def balance_check(self):        
        check_balance = input('Do you want to check your balance? yes/no \n')
        if (check_balance == 'yes'):
            print('Your balance is {}'.format(self.balance))
        else:
            print('Thank you for banking with us')

                


