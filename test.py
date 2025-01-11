import random

def guess_the_number():
    print("\nWelcome to the 'Guess the Number' game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it in as few attempts as possible.\n")

    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    while not guessed_correctly:
        try:
            # Get user's guess
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
                guessed_correctly = True

        except ValueError:
            print("⚠️ Please enter a valid number!")

def main_menu():
    while True:
        print("\n========== Main Menu ==========")
        print("1. Play 'Guess the Number'")
        print("2. Instructions")
        print("3. Exit")
        print("================================")

        try:
            choice = int(input("Enter your choice (1-3): "))

            if choice == 1:
                guess_the_number()
            elif choice == 2:
                print("\n🔍 **Instructions**")
                print("1. The game will generate a random number between 1 and 100.")
                print("2. You must guess the number. After each guess, you'll be told if it's too high or too low.")
                print("3. Keep guessing until you find the correct number!")
                print("4. Try to guess in as few attempts as possible.\n")
            elif choice == 3:
                print("\nThank you for playing! Goodbye 👋")
                break
            else:
                print("⚠️ Invalid choice! Please select an option between 1 and 3.")
        except ValueError:
            print("⚠️ Please enter a valid numeric option!")

if __name__ == "__main__":
    main_menu()
