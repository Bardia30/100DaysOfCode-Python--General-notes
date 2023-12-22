def fizz_buzz(input):
    if not isinstance(input, int):
        return "input must be an integer"
    if input % 15 == 0:
        return "FizzBuzz"
    if input % 5 == 0: 
        return "Buzz"
    if input % 3 == 0:
        return "Fizz"
    else:
        return input


print(fizz_buzz(10))