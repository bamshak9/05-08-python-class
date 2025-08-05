amount = float(input("How much: "))
discount20 = 0.2*amount
discount20p = amount - discount20
discount10 = 0.1*amount
discount10p = amount - discount10
discount5 = 0.05*amount
discount5p = amount - discount5
if amount >50000:
    print(f"Your discount is #{discount20} and you should pay {discount20p}")
elif amount <=50000 and amount>30000:
    print(f"Your discount is #{discount10} and you should pay {discount10p}")
elif amount <=30000 and amount>10000:
    print(f"Your discount is #{discount5} and you should pay {discount5p}")
else:
    print(f"You have no discount and you should pay {amount}")
   
   
