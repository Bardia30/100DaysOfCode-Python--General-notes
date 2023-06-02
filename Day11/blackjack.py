############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:

## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run
from art import logo
import random

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

is_playing = True
while is_playing:
    play_blackjack = input("Do you want to play a game of blackjack? Type 'y' or 'n': ")
    if play_blackjack == 'y':
        print("game begins")
        computer_hand = []
        user_hand = []
        
        

        def pick_card():
            picked_card = cards[random.randint(0,12)]
            return picked_card
        
        
        computer_hand.append(pick_card()) 
        computer_hand.append(pick_card())
        user_hand.append(pick_card())
        user_hand.append(pick_card())
        print(f"user cards: {user_hand}")
        print(f"computer hand: {computer_hand}")
        computer_sum = sum(computer_hand)
        user_sum = sum(user_hand)
        
        # def dealer_card_pick():
        #     while computer_sum <= 21:
        #         if computer_sum <= 16:
        #             computer_hand.append(pick_card())
        #             computer_sum = sum(computer_hand)
        #         else:
        #             break
        #     return computer_sum
        
        while user_sum <= 21:
            for card in user_hand:
                if card == 11 and user_sum > 21:
                    card = 1
            print(f"user's sum: {user_sum}")
            user_choice = input("do you want another card? type 'y' or 'n': ")
            
            if user_choice == 'y':
                user_hand.append(pick_card())
                user_sum = sum(user_hand)
                print(f"user cards: {user_hand}")
            else:
                print(f"user stays with hand: {user_hand}")
                break
            
        while computer_sum <= 21:
            if computer_sum <= 16:
                computer_hand.append(pick_card())
                computer_sum = sum(computer_hand)
                print(f"computer hand: {computer_hand}")
            else:
                print(f"computer hand: {computer_hand}")
                break
        if user_sum > 21: 
            print("you busted")
        elif computer_sum > 21: 
            print("dealer busted, you win")
        elif computer_sum > user_sum:
            print("you lose")
        elif user_sum > computer_sum:
            print("you win")
        elif user_sum == computer_sum:
            print("draw")






    else:
        is_playing = False

