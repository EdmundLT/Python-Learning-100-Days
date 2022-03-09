from art import logo, vs
from data import data
import random


def higher_lower():
    game_over = False
    a = random.choice(data)
    user_point = 0
    while game_over == False:
        b = random.choice(data)
        a_name = a["name"]
        a_follower_count = a["follower_count"]
        a_description = a["description"]
        a_country = a["country"]
        b_name = b["name"]
        b_follower_count = b["follower_count"]
        b_description = b["description"]
        b_country = b["country"]
        print(logo)
        print(f"Compare A: {a_name}, {a_description}, from {a_country}")
        print(vs)
        print(f"Compare B: {b_name}, {b_description}, from {b_country}")
    # compare(a, b):
        if a_follower_count > b_follower_count:
            answer = "A"
        else:
            answer = "B"

        user_answer = input("Who has more follwers? Type 'A' or 'B': ")

        if user_answer == answer and b_follower_count > a_follower_count:
            user_point += 1
            print(f"Correct! Your current score is {user_point}.")
            a = b
        elif user_answer == answer:
            user_point += 1
            print(f"Correct! Your current score is {user_point}.")

        if user_answer != answer:
            print(f"You are incorrect. Your final score: {user_point}.")
            game_over = True


higher_lower()
