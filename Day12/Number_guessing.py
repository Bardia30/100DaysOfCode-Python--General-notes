import random 

print("Welcome to number guessing game!")

chosen_number = random.randint(0,100)
print(f"psst, the chosen number is: {chosen_number}")
    
user_wins = False

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'hard':
    attempts = 5
else: 
    attempts = 10
print(f"you have {attempts} attempts remaining")


def compare(user_guess, chosen_number):
    user_won = False
    if user_guess == chosen_number:
        user_won = True
    return user_won

def low_or_high(user_guess, chosen_number):
    if user_guess < chosen_number:
        result = "too low"
    elif user_guess > chosen_number:
        result = "too high"
    return result

while  not user_wins and attempts > 0:
    #make user guess
    user_guess = int(input("make a guess: "))
    
    #compare
    user_won = compare(user_guess, chosen_number)
    if not user_won:
        attempts = attempts - 1
        result = low_or_high(user_guess, chosen_number)
        print(f"your guess was {result}")
        print(f"you have {attempts} attempts remaining")
    else:
        user_wins = True
        print("you have won")
        break
    if attempts == 0:
        print("sorry, you ran out of attemps. ")
        break
    #decrease from attemps
    #tell if the guess is too high or too low
    #tell guess again. 
