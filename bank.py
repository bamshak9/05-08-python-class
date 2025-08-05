print("""
        1. Onboard customer
        2. Withdraw cash
        3. Add Cash
        4. Transfer
        5. Change pin
""")
customers =[{"Name":"Bamshak Luka", "Amount":350000, "Pin":1234, "ID": 1}, {"Name":"Kyenpiya Luka", "Amount":350000, "Pin":1234, "ID": 2}]
automatic_id = 3476892
user_input = int(input("Select an option: "))
if user_input >=1 and user_input <=5:
    if user_input ==1:
        user_name = input("Name: ")
        user_amount = float(input("Amount: "))
        user_pin = input("pin: ")
        if len(user_pin) ==4:
            new_customer = {"Name":user_name, "Amount":user_amount, "Pin":int(user_pin), "ID": automatic_id}
            customers.append(new_customer)
        else:
            print("invalid pin length")
    if user_input ==2:
        user_id =int(input("ID: "))
        for customer in customers:
            if user_id != customer["ID"]:
                continue
                print("User does not exist")
            else:
                amount = float(input("Enter Amount to withdraw: "))
else:
    print("Invalid selected action")
print(customers)
automatic_id +=1
