import random
def number_gussing_game():
    secret_number = random.randint(1, 100)
    print(secret_number)
    print("Welcome to the Number Gussing game")
    print("I have the number between 1 to 100 , Can you guess it ?")
    attempts = 0
    guess = None
    while guess !=secret_number:
        guess = int(input("Enter Your Guess"))
        attempts = attempts + 1
        if guess<secret_number:
            print("Too low , Try again")
        elif guess > secret_number:
            print("Too high, Try again")
        else:
            print("Congratulations you have guessed the correct number")
            print("The number of attempts in guessing the correct number is", attempts)
number_gussing_game()