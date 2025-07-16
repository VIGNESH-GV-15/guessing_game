import random

def guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    guess = None

    print("🎲 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?\n")

    while guess != secret_number:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("🔻 Too low! Try again.\n")
            elif guess > secret_number:
                print("🔺 Too high! Try again.\n")
            else:
                print(f"✅ Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
        except ValueError:
            print("❌ Invalid input! Please enter a number.\n")

# Run the game
if __name__ == "__main__":
    guessing_game()