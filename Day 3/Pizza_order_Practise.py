print("Welcoe to Python pizza Deliveries !")
size = input("What size do you want ? S, M or L !!")
Peparoni =input("Do you want peparoni on your pizza ? Y or N : ")
extra_cheese = input("Do you want Extra chees ? Y or N !!")

bill = 0
if size =="S":
    bill+=15
elif size =="M":
    bill+=20
elif size =="L":
    bill +=25
else:
    print("You type the Wrong Input !!")


if Peparoni =="Y":
    if size=="S":
        bill+=2
    else:
        bill+=3

if extra_cheese=="Y":
    bill+=1

print(f"Final Bill is :${bill}.")
