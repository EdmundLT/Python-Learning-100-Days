from art import logo
import random


def start_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty: Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return easy()
    if difficulty == "hard":
        return hard()


def easy():
    answer = random.randint(1, 101)
    attempts = 10
    game_end = False
    while attempts != 0 and game_end == False:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guessing = int(input("Make a guess: "))
        if guessing == answer:
            print(f"You got it! The answer was {answer}.")
            game_end = True
        elif guessing > answer:
            print("Too high.")
            print("Guess again.")
            attempts -= 1
            if attempts == 0:
                print("You've run out of guesses, you lose.")
        elif guessing < answer:
            print("Too low.")
            print("Guess again.")
            attempts -= 1
            if attempts == 0:
                print("You've run out of guesses, you lose.")


def hard():
    answer = random.randint(1, 101)
    attempts = 5
    game_end = False
    while attempts != 0 and game_end == False:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guessing = int(input("Make a guess: "))
        if guessing == answer:
            print(f"You got it! The answer was {answer}.")
            game_end = True
        elif guessing > answer:
            print("Too high.")
            print("Guess again.")
            attempts -= 1
            if attempts == 0:
                print("You've run out of guesses, you lose.")
        elif guessing < answer:
            print("Too low.")
            print("Guess again.")
            attempts -= 1
            if attempts == 0:
                print("You've run out of guesses, you lose.")


start_game()
