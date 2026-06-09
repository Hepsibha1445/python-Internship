import random

def number_guessing_game():
    secret = random.randint(1, 100)
    attempts = 0

    print("🎯 Welcome to the Number Guessing Game!")
    print("I've picked a number between 1 and 100. Can you guess it?\n")

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("⚠️  Please enter a valid number.\n")
            continue

        if guess < 1 or guess > 100:
            print("⚠️  Number must be between 1 and 100.\n")
            continue

        attempts += 1

        if guess < secret:
            print(f"🔼 Too low! Try higher.\n")
        elif guess > secret:
            print(f"🔽 Too high! Try lower.\n")
        else:
            print(f"🎉 Correct! The number was {secret}.")
            print(f"✅ You got it in {attempts} attempt{'s' if attempts > 1 else ''}!")
            break

number_guessing_game()