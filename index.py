import random

def number_guesser():
    print("Welcome to the Number Guesser Game!")
    try:
        # Get the range from the user
        start_range = int(input("Enter the start of the range: "))
        end_range = int(input("Enter the end of the range: "))

        if start_range >= end_range:
            print("Invalid range! Start of the range must be less than the end.")
            return
        
        # Generate a random number within the specified range
        number_to_guess = random.randint(start_range, end_range)
        guessed = False

        print(f"I have selected a number between {start_range} and {end_range}. Can you guess it?")
        
        while not guessed:
            try:
                # Get the user's guess
                user_guess = int(input("Enter your guess: "))

                if user_guess < number_to_guess:
                    print("Too low! Try again.")
                elif user_guess > number_to_guess:
                    print("Too high! Try again.")
                else:
                    print(f"Congratulations! You guessed it right. The number was {number_to_guess}.")
                    guessed = True
            except ValueError:
                print("Please enter a valid number.")
    except ValueError:
        print("Invalid input! Please enter numerical values for the range.")

# Run the game
number_guesser()
