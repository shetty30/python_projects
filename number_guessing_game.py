import random

secret_number = random.randint(1, 100)
attempts = 0

print ("Welcome to the Number Guessing Game!")
print ("I'm thinking of a number between 1 and 100.")

while True:
    try:
        guess = int(input("Make a guess: "))
        attempts += 1

        if guess < 1 or guess > 100:
            print("Please guess a number within the range of 1 to 100.")
            continue
        if guess < secret_number:
            print("Too low.")
        elif guess > secret_number:
            print("Too high.")

        else:
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
            break
    except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")
        
    



        
     





