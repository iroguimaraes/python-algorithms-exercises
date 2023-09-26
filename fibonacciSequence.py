giveNumber = input("Write a number: ")
value = 1
previousValue = 0
storedValue = 0
index = 0
sequence = []



try:
    maxNumber = int(giveNumber)
    print(f"You entered the integer: {giveNumber}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")



while value < maxNumber:
    sequence.insert(index, value)
    storedValue = value
    value = previousValue + value
    previousValue = storedValue
    index += 1

print("fibonacci sequence: ", sequence)