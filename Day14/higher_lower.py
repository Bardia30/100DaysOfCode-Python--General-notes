from art import logo, vs
from game_data import data
import random
import os

#create a score variable
score = 0
#pick a dict from the data list --> func pick_data()
#asign to variable A 
A = data[random.randint(0,len(data)-1)]

def pick_index():
    index = random.randint(0,len(data)-1)
    return index

def pick_B (A):
    index_B = pick_index()
    B = data[index_B]
    while A == B:
        pick_B(A)
    return B


B = pick_B(A)

def display(a,b):
    print(logo)
    name_a = a["name"]
    desc_a = a["description"]
    country_a = a["country"]
    name_b = b['name']
    desc_b = b['description']
    country_b = b['country']
    print(f"compare A: {name_a}, a {desc_a}, from {country_a}")
    print(vs)
    print(f"compare B: {name_b}, a {desc_b}, from {country_b}")


user_lost = False

def compare(a,b):
    winner = 'A'
    follower_a = a['follower_count']
    follower_b = b['follower_count']
    if follower_a < follower_b:
        winner = "B"
    return winner


while not user_lost:
    #pick a dict from the data list --> func pick_data()
    #asign to variable B 
    print(f"score: {score}")
    if score != 0:
        old_A = A
        A = B
        B = pick_B(old_A)
    else:
        B = pick_B(A)
    #replace B with A
    #Show the results --> func display(A,B)
    display(A,B)
    # prompt user for desicion making: A or B? 
    user_decision = input("which one has higher followers? 'A' or 'B': ").upper()
    # check if A is Higher or B --> compare(A, B)
    answer = compare(A,B)
    if user_decision == answer:
        score += 1
        os.system("cls")
        print("that was correct, keep going")
    else:
        os.system('cls')
        print("game over")
        print(f"score: {score}")
        user_lost = True
    # if user guesses correct: 
    #     continue playing
    #     add one point to scores.
    #      
    # else:
    #     game Over
    #     show scores. 