inputNumber = input("Write a number: ")

try:
    setNumber = int(inputNumber)
    print(f"You entered the integer: {setNumber}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")

# using recursive function this time
def factorialFunction(n):
    if n < 0:
        return None  
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorialFunction(n - 1)
    
factorialResult = factorialFunction(setNumber)
if factorialResult is not None:
    print(f"The factorial of {setNumber} is {factorialResult}")
else:
    print("Factorial is not defined for negative numbers.")