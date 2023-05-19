#calculator
from art import logo


def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def divide(n1,n2):
    return n1 / n2

def multiply(n1,n2):
    return n1 * n2


def calculate(first_number, operator, second_number):
    operations = {
        "+":add,
        "-":subtract,
        "/":divide,
        "*":multiply,
    }
    result = operations[operator](first_number, second_number)
    print(result)
    # if operator == "+":
    #     result = add(first_number, second_number)
    #     print(result)
    # elif operator == "-":
    #     result = subtract(first_number, second_number)
    #     print(result)
    # elif operator == "/":
    #     result = divide(first_number, second_number)
    #     print(result)
    # elif operator == "*":
    #     result = multiply(first_number, second_number)
    #     print(result)
    # else:
    #     print("enter a valid operator")
    #     return
    return result



def run_calculator():
    calculator_running = True
    print(logo)
    print("welcome to the Python Calculator")
    first_number = float(input("what is the first number?: "))
    while calculator_running:
        result = calculate(first_number, input("what is the operator? enter +,-,/, or *: "), float(input("what is the second number?: ")))
        keep_running = input("would you like to keep using the result? enter 'yes' or 'no': ")
        if keep_running == 'yes':
            first_number = result
        else:
            calculator_running = False
            return "thank you, program is finished"



print(run_calculator())