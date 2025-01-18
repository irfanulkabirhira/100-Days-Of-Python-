print("Welcome to the Roller Coaster!")
height = int(input("What is your height in cm? "))  # Convert input to integer
bill = 0

if height >= 120:  # Compare integers
    print("You can ride the roller coaster!")
    age = int(input("What is your age? "))  # Convert input to integer
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Teen tickets are $7.")
    elif 45 <= age <= 55:
        print("Everything is going to be okay! Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N ").strip().upper()  # Normalize input
    if wants_photo == "Y":
        bill += 3
    print(f"Your final bill is ${bill}.")
else:
    print("Sorry, you need to be taller to ride. Hope for the best!")
