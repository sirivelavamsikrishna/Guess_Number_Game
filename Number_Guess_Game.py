import random
import time

def get_attempts():
    print("\nPlease select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")
    
    choice = input("Enter your choice (1/2/3): ")
    difficulty = {"1": 10, "2": 5, "3": 3}
    return difficulty.get(choice, 5)  # Default to Medium if invalid choice

def play_game():
    print("\nWelcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    attempts = get_attempts()
    number = random.randint(1, 100)
    start_time = time.time()
    
    print(f"Great! You have {attempts} chances to guess the number. Let's start!")
    
    for attempt in range(1, attempts + 1):
        guess = input("Enter your guess: ")
        
        if not guess.isdigit():
            print("Invalid input! Please enter a number.")
            continue
        
        guess = int(guess)
        
        if guess == number:
            end_time = time.time()
            print(f"Congratulations! You guessed the correct number in {attempt} attempts.")
            print(f"Time taken: {round(end_time - start_time, 2)} seconds.")
            return attempt
        elif guess < number:
            print("Incorrect! The number is greater than your guess.")
        else:
            print("Incorrect! The number is less than your guess.")
    
    print(f"Sorry! You've used all your attempts. The number was {number}.")
    return None

def main():
    high_score = None
    
    while True:
        score = play_game()
        
        if score and (high_score is None or score < high_score):
            high_score = score
            print(f"New high score: {score} attempts!")
        
        replay = input("Do you want to play again? (yes/no): ").strip().lower()
        if replay != "yes":
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
