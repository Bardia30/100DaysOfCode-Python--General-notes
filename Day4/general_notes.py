# Exercise4.1 - Heads or Tails

# import random

# random_num = random.randint(0,1)


# if random_num == 0:
#     print("Heads")
# else: 
#     print("Tails")

#______________________________________________________________________
# Data Structure: way to organize and store data 
# List --> a data structure, like array in JavaScript

# Exercise 2 

# # Import the random module here
# import random
# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# # payer = random.choice(names)


# players_count = len(names)

# random_number = random.randint(0,players_count-1)

# payee = names[random_number]

# print(f"{payee} is going to buy the meal today!")
# print(f"random num: {random_number}, payee: {payee}")
#_____________________________________________________________
#Exercise 3 - Treasure map 
# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
column = int(position[0]) - 1
row = int(position[1]) - 1

map[column][row] = 'X'



#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")