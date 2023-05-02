# %%
print("nice nice")

# %%
print("Day 1 - Python Print Function \nThe function is declared like this: \nprint('what to print')")

# %% [markdown]
# string concatenation

# %%
print("Bardia"+" "+"Dehbasti")

# %% [markdown]
# Note: Python is sensitive to indentation --> gives indentation error if unnecessary indentation is there
# 
# Excercise2: fix the error below:

# %%
print(Day 1 - String Manipulation")
print("String Concatenation is done with the "+" sign.")
  print('e.g. print("Hello " + "world")')
print(("New lines can be created with a backslash and n.")

# %%
print("Day 1 - String Manipulation")
print("String Concatenation is done with the " + '"+"'+ " sign.")
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

# %%
#input function
print("Hello " + input ("what is your name? "))

# %%
# Exercise 1.3 
print(len(input("What is your name? : ")))
user_input = input("What is your age?: ")
user_age_length = str(len(user_input))
print("user is " + user_input + " years old, and their name has "+ user_age_length + " digits")

# %%
#Exercise 1.4
#INSTRUCTIONS: Write a program that switches the values stored in the variables a and b.
#Example Input: 
# a: 3
# b: 5

#Example output
# a: 5
# b: 3

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
c = a
a = b 
b = c




#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)



# %%
#  Project Day One 
#1. Create a greeting for your program.
print("Hellow there, dear user!")

#2. Ask the user for the city that they grew up in.
user_city = input("which city did you grew up in?Please enter: \n")
#3. Ask the user for the name of a pet.
user_pet = input("What is the name of yout pet?: \n")
#4. Combine the name of their city and pet and show them their band name.
print("your band name is: " + user_city + " " +  user_pet)
#5. Make sure the input cursor shows on a new line:


