jamb_score = int(input("Enter your Score: "))
if jamb_score >400:
    print("Your score is not true and valid")
elif jamb_score >=250:
    print("You are eligible for medicine")
elif jamb_score >=200 and jamb_score<250:
    print("You are eligible for Engineering and Science")
elif jamb_score >=180 and jamb_score<200:
    print("You are eligible for Education and Social Science")
else:
    print("You are not eligible for admission this year")

