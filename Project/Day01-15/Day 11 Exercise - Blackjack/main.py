from art import logo
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def start_game():
    if input(f"Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        return game_opening()
    else:
        print("Okay.")


def game_opening():
    print(logo)
    user_hands = []
    com_hands = []
    user_hand_1 = random.choice(cards)
    user_hand_2 = random.choice(cards)
    com_hand_1 = random.choice(cards)
    com_hand_2 = random.choice(cards)
    user_hands.append(user_hand_1)
    user_hands.append(user_hand_2)
    com_hands.append(com_hand_1)
    com_hands.append(com_hand_2)
    user_score = sum(user_hands)
    com_score = sum(com_hands)

    print(f"Your cards: {user_hands}, current score: {user_score}")
    print(f"Computer's first card: {com_hands[0]}")
    ##blackjack check##
    if user_score == 21:
        print("You have blackjack. You win")
    if com_score == 21:
        print("Computer have blackjack. You lose.")

    ans = input("type 'y' to get another card, type 'n' to pass: ")
    while ans == "y":
        user_hands.append(random.choice(cards))
        user_score = sum(user_hands)

        print(f"Your cards: {user_hands}, current score: {user_score}")
        while com_score < 17:
            com_hands.append(random.choice(cards))
            com_score = sum(com_hands)
            print(f"computer's cards: {com_hands[0]}, {com_hands[1]}")
        if user_score > 21:
            if 11 in user_hands:
                user_hands.remove(11)
                user_hands.append(1)
                user_score = sum(user_hands)
                if user_score > 21:
                    print(f"You have {user_score}. computer win.")
        if com_score > 21:
            if 11 in com_hands:
                com_hands.remove(11)
                com_hands.append(1)
                com_score = sum(com_hands)
                if com_hands > 21:
                    print(f"computer have {com_score}. you win.")
        ans = input("type 'y' to get another card, type 'n' to pass: ")
    if ans == "n":
        user_score = sum(user_hands)
        com_score = sum(com_hands)
        print(f"Your final hand: {user_hands}, final score: {user_score}")
        print(f"Computer final hand: {com_hands}, final score: {com_score}")
        if user_score > com_score:
            print(f"You have {user_score}. You win.")
        if user_score < com_score:
            print(f"You have {user_score}. You lose.")
        if user_score == com_score:
            print("Draw.")
            return start_game()


start_game()
