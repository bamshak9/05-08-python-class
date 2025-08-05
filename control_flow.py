'''
18-25: Regular
26-35: VIP
36-40: vvip
'''
age = int(input("Age: "))
if age >=18 and age<26:
    print("Regular")
elif age >=26 and age<36:
    print("VIP")
elif age >=36 and age<41:
    print("VVIP")
elif age >40:
    print("Go home old man")
else:
    print("Go home or we will call your mum")


