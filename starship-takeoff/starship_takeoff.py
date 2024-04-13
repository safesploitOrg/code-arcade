import random

def starship_takeoff():
    target_number = random.randint(1, 500)
    lives = 10
    
    print("Welcome to Starship Takeoff!")
    print("You have to guess the number between 1 and 500.")
    print(f"You have {lives} lives. Let's start!")

    while lives > 0:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        
        if guess == target_number:
            print("Congratulations! You've successfully guessed the number. The starship takes off!")
            break
        elif guess < target_number:
            print("Too low!")
        else:
            print("Too high!")
        
        lives -= 1
        print(f"You have {lives} {'life' if lives == 1 else 'lives'} left.")

    else:
        print("The aliens got you! Game over.")

if __name__ == "__main__":
    starship_takeoff()
