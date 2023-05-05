# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? :"))


# if height > 120:
#     print("You can ride")
# else:
#     print("Sorry, you short af")

#_____________________________________________
# Day 3 Exercise one
# Instructions
# Write a program that works out whether if a given number is an odd or even number.

# # 🚨 Don't change the code below 👇
# number = int(input("Which number do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# if number % 2 == 0:
#     print("this number is even")
# else:
#     print("this number is odd")
#________________________________________________________________________________
# Exercise 3.2
# BMI 2.0

# 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# BMI = round(weight / (height**2))

# if BMI < 18.5 and BMI > 0:
#     print(f"Your BMI is {BMI}, you are underweight")
# elif BMI > 18.5 and BMI < 25: 
#     print(f"Your BMI is {BMI}, you are normal weight")
# elif BMI > 25 and BMI < 30:
#     print(f"Your BMI is {BMI}, you are slightly overweight")
# elif BMI > 30 and BMI < 35: 
#     print(f"Your BMI is {BMI}, you are obese")
# else:
#     print(f"Your BMI is {BMI}, you are clinically obese")

# #_______________________________________________________________
# # Exercise 3.3 Leap Year
# # 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# if year % 4 == 0:
#     if year % 100 == 0 and year%400 !=0:
#         print("not leap year")
#     else:
#         print("leap year")
# else:
#     print("not leap year")
#____________________________________________________________
# Exercise 3.4 Pizza order 
# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill.

# Small Pizza: $15

# Medium Pizza: $20

# Large Pizza: $25

# Pepperoni for Small Pizza: +$2

# Pepperoni for Medium or Large Pizza: +$3

# Extra cheese for any size pizza: + $1

# 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# price = 0
# if size.lower() == "l":
#     price += 25
# elif size.lower() == "m":
#     price += 20
# else:
#     price += 15
# if add_pepperoni == "Y":
#     if size == "L" or size == "M":
#         price += 3
#     else:
#         price += 2
# if extra_cheese == "Y":
#     price += 1

# print(f"your final bill is ${price}")
# _____________________________________________________
# # Exercise 3.5 Love calculator
# # 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n").upper()#input("What is your name? \n")
# name2 = input("What is their name? \n").upper()#input("What is their name? \n")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# names = name1+name2

# list_of_true = ["T", "R", "U", "E"]
# list_of_love = ["L","O","V","E"]


# count1 = 0
# count2 = 0
# for i in range(len(list_of_true)):
#     count1 += names.count(list_of_true[i])
#     print(count1)
# for i in range(len(list_of_love)):
#     count2 += names.count(list_of_love[i])

# total_count = int(str(count1)+str(count2))
# print(count1, count2)
# if total_count<10 and total_count>90:
#     print(f"Your score is {total_count}, you go together like coke and mentos.")
# elif total_count > 40 and total_count < 50: 
#     print(f"Your score is {total_count}, you are alright together.")
# else:
#     print(f"Your score is {total_count}.")