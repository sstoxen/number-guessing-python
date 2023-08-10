from random import randint

lower_number, higher_number = 1, 10
print(f"Guess a number in the range from {lower_number} to {higher_number}.")
random_number: int = randint(lower_number, higher_number)
guessed = False

while not guessed:
    try:
        guess: int = int(input("Guess: "))
        if guess > random_number:
            print("The number is lower.")
        elif guess < random_number:
            print("The number is higher.")
        else:
            print("You guessed it!")
            guessed = True
    except ValueError as e:
        print("Please enter a valid integer (no decimal!).")

