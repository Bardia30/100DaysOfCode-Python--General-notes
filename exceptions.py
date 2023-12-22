try:
    file = open("app.py") 
    age = int(input("age: "))
    xfactor = 10 / age
    
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid input for age.")
else: 
    print("no exceptions were thrown")
finally: 
    file.close()