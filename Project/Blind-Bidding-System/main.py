from tracemalloc import start
from art import logo

bid = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest:
            highest = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest}")


while not bidding_finished:
    print(logo)
    name = input("What is your name?: ")
    price = int(input("What is your price?: "))
    bid[name] = price
    ans = input("Are there any other bidders?: Type 'yes' or 'no'.").lower()
    if ans == "no":
        bidding_finished = True
        find_highest_bidder(bid)
    elif ans == "yes":
        bidding_finished = False
        print("\033c")
