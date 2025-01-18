print("Welcome to the Tip Calculator !")
bill = float(input("What is the total Bill ? $"))
tip = int(input("what percentage would you like to give ? 10 , 12, 15"))
bil_with_tip = tip/100*bill +bill
print(bil_with_tip)