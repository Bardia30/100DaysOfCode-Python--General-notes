#Day 2 Project:
# Tip Calculator

# Instructions
# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6

# Format the result to 2 decimal places = 33.60

# Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Example Input
# Welcome to the tip calculator!
# What was the total bill? $124.56
# How much tip would you like to give? 10, 12, or 15? 12
# How many people to split the bill? 7

# Example Output
# Each person should pay: $19.93

print("welcome to the the tip calculator")

total_bill = float(input("What was the total bill?:  \n"))

tip_amount = float(input("How much tip would you like to give? 10, 12, or 15?: \n"))/100 + 1.0

amount_of_people = int(input("How many people to split the bill?: \n"))

per_person_pre_tip = total_bill/amount_of_people

per_person_total = round(per_person_pre_tip*tip_amount , 2)

print(f"each person pay: ${per_person_total}")