account_balance = 10000
amount = float(input("How much do you want?: "))
balance = account_balance - amount
if amount>10000:
    print("Insufficient funds")
elif amount <0:
    print("That operation is not possible, nice try wise guy")
elif amount%1000 !=0:
    print("Sorry, you cannot make the transaction")
else:
    print(f"You have withdrawn {amount} and your current balance is {balance}")
print("Thank you for your patronage")
if amount <= account_balance and amount >=0 and amount%1000==0:
    account_balance = balance
else:
    account_balance = account_balance-0
print(f"Final account:", account_balance)

