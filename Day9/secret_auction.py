import os
from logo import logo

# print(logo)
# print("Welcome to the secret auction program.")
# user_name = input("What is your name?: ")
# user_bid = input("What is your bid?: ")
# other_bidders = input('Are there any other bidders?: ')

bids = []


def add_bid(user_name, user_bid):
    new_bid = {
        "name": user_name,
        "bid":user_bid
    }
    bids.append(new_bid)

def show_winner(list):
    global winner
    bid_amount=0
    for user_bid in list:
        if user_bid['bid']>bid_amount:
            bid_amount = user_bid['bid']
            winner = user_bid['name']
    return f"and the winner is: {winner}, with the highest bid being at ${bid_amount}"

def run_bid():
    is_running=True
    while is_running:
        print(logo)
        print("Welcome to the secret auction program.")
        user_name = input("What is your name?: ").lower()
        user_bid = int(input("What is your bid?: "))
        other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
        add_bid(user_name, user_bid)
        if other_bidders == 'no':
            is_running = False
            os.system('cls')
            print(show_winner(bids))
        else:
            os.system('cls')


run_bid()