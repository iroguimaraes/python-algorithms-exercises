setNumber = input("Write the integer value: ")
counter = 1
value = 0
factorialValue = 0

try:
    inputNumber = int(setNumber)
    print(f"You entered the integer: {setNumber}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")

factorialValue = inputNumber
value = inputNumber
while inputNumber > counter:
    value = value * (inputNumber - 1)
    inputNumber -=1


if factorialValue == 0 or factorialValue == 1:
    value = 1
if factorialValue < 0:
    print("Invalid input. Please enter a value equal or greater than 0.")
else:
    print("factorial is: ", value)