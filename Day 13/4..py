# intintage = int(input("How old are ? "))
# if age > 18:
#     print("You can druve the car")


try:
    age = int(input("How old are ? "))
except ValueError:
    print("you have typed in an Invalied Please Type something Numarical ")
    age = int(input("How old are you ?"))

if age > 18:
    print(f"You can drive at age {age}.")
else:
    print(f"Sorry You can not drive at this age {age}.")

