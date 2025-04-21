import random

def number_guessing_game():

    print("Guess a number between 1 and 100.")
    
    number_range = random.randint(1, 50) #Generate a random number between 1 and 50
    number_of_guesses = 0 # Initialize the number of guesses
    guess_attempts = 3 #Maximum number of attempts

    while number_of_guesses < guess_attempts:
        try:
            guess = int(input("Enter a number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        number_of_guesses += 1 # Increment the number of guesses

        if guess < number_range:
            print("Too low!")
        elif guess > number_range:
            print("Too high!")
         
        else:
            print(f"Congratulations! You guessed the number {number_range} in {number_of_guesses} attempts.")
            break
    else:
        print("Sorry, you've used all your attempts. The number was", number_range)

number_guessing_game()