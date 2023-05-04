# Data types

#1 Strings  "hello"
#2 Integer 23
#3 float 34.45

# To check the data type => type(sth) (a function)
# type casting: changing the data type from one to another
# to string: str() function
# to float: float()
# to integer: int()

#------------------------------------------------------------
#Exercise2.1
#Instruction: Write a program that adds the digits in a 2 digit number. 
#e.g. if the input was 35, then the output should be 3 + 5 = 8

# 🚨 Don't change the code below 👇
# two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

# if len(two_digit_number) != 2:
#     print('has to be digits')
# else: 
#     first_digit = int(two_digit_number[0])
#     second_digit = int(two_digit_number[1])
#     digits_sum = first_digit + second_digit
    #print(str(first_digit) + ' + ' +str(second_digit)+ ' = '+ str(digits_sum) )
#_______________________________________________________
# Math operators
# addition => +
# sub      => -
# Mult     => *
# divide   => /
# power    => **
# remainder=> %
# flr div  => //

#________________________________________________________________
#Exercise 2.2 BMI Calculator
# Instruction : 
# Write a program that calculates the Body Mass Index (BMI) 
# from a user's weight and height.

# The BMI is a measure of someone's weight taking into 
# account their height. e.g. If a tall person 
# and a short person both weigh the same amount, 
# the short person is usually more overweight.

# The BMI is calculated by dividing a 
# person's weight (in kg) by the square of their height (in m):
# 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# height = float(height)
# weight = float(weight)

# BMI = round(weight / (height**2))
# print('Your BMI is: '+str(BMI))
#________________________________________________________________

# round(float, decimal places) -> rounds number to specified decimal places
# num = num +1 => num += 1
# F strings f"the string {variable}"
#_____________________________________________________________________
# Exercise 2.3 how many weeks left of life if live to 90
#Instructions: 
# Create a program using maths and f-Strings that tells us how many 
#days, weeks, months we have left if we live until 90 years old.

# It will take your current age as the input and output a message 
#with our time left in this format:

# You have x days, y weeks, and z months left.

# Where x, y and z are replaced with the actual calculated numbers.
# 🚨 Don't change the code below 👇
# age = input("What is your current age? ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# years_left = 90 - int(age)
# months_left = years_left *12 
# weeks_left = years_left * 52 
# days_left = years_left * 365

# print(f"you have {months_left} months, {weeks_left} weeks, and {days_left} days left.")
#___________________________________________________________________________________________________




