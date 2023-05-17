# Challenge#1 how many cans of paint is needed?

# #Write your code below this line 👇
import math

# # 1 can of paint can cover 5m2 of wall
# # Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
def paint_calc(height, width, cover):
    number_of_cans = math.ceil((height*width)/cover)
    return f"you'll need {number_of_cans} cans of paint"




# #Write your code above this line 👆
# # Define a function called paint_calc() so that the code below works.   

# # 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# print(paint_calc(height=test_h, width=test_w, cover=coverage))

#Challenge2: prime number checker
#Write your code below this line 👇
def prime_checker(number):
    if number == 2:
            return "It's a prime number"
    else:
        for num in range(2,number):
            #print(num)
            
            if number % num != 0:
                return "It's a prime number"
            else:
                return "It's not prime number"




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
print(prime_checker(number=n))