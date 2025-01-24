import random

def guess_the_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Start a loop to guess
    while not guessed_correctly:
        try:
            #  Guess the number
            player_guess = int(input("Enter your guessing number: "))
            attempts += 1

            # Player guess number (too low), (too high), and correct
            if player_guess < number_to_guess:
                print("Too low! Think High.")
            elif player_guess > number_to_guess:
                print("Too high! Think low.")
            else:
                guessed_correctly = True
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
        except ValueError:
            print("Defeat, Better luck next time. please try again later.")

# Start Game
guess_the_number()

