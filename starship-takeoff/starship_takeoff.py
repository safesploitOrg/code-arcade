import random
import time
import pygame
import os

def print_starship():
    print("           ____")
    print("          /    \\")
    print("    _____/      \\_____")
    print("   |                 |")
    print("   |    STARSHIP    |")
    print("   |      _ _ _     |")
    print("   |     | | | |    |")
    print("   |_____|_|_|_|____|")
    print("         /_____\\")
    print("         |     |")
    print("         |_____|")
    print("\n")

def play_sound(sound_file):
    pygame.mixer.init()
    file_path = os.path.join(os.path.dirname(__file__), sound_file)
    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
    except FileNotFoundError:
        print(f"Error: Sound file '{sound_file}' not found. Sound effect will not be played.")
    else:
        print("\nThe aliens got you! Game over.")

def check_integrity():
    required_files = ["success.wav", "failure.wav"]
    missing_files = []
    for file in required_files:
        if not os.path.isfile(file):
            missing_files.append(file)
    
    if missing_files:
        print("Error: The following required files are missing:")
        for file in missing_files:
            print(f" - {file}")
        return False
    else:
        print("All required files are present. Launching the game...")
        return True

def starship_takeoff():
    target_number = random.randint(1, 500)
    lives = 1
    
    print("Welcome to Starship Takeoff!")
    print("You have to guess the number between 1 and 500.")
    print(f"You have {lives} lives. Let's start!\n")
    
    # Print starship ASCII art
    print_starship()
    
    # Initialize pygame
    pygame.init()
    
    while lives > 0:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        
        if guess == target_number:
            print("\nCongratulations! You've successfully guessed the number. The starship takes off!\n")
            # Play success sound
            play_sound("success.wav")
            # Print starship taking off animation
            for i in range(3):
                print_starship()
                time.sleep(0.5)
                print("\033[F" * 13)  # Move cursor up 13 lines
            break
        elif guess < target_number:
            print("Too low!")
        else:
            print("Too high!")
        
        lives -= 1
        print(f"You have {lives} {'life' if lives == 1 else 'lives'} left.")

    else:
        print("\nThe aliens got you! Game over.")
        # Play failure sound
        play_sound("failure.wav")

if __name__ == "__main__":
    check_integrity()
    starship_takeoff()
