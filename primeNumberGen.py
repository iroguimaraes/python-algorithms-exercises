inputNumberStart = input("Write a start number: ")
inputNumberEnd = input("Write a end number: ")


try:
    setNumberStart = int(inputNumberStart)
    setNumberEnd = int(inputNumberEnd)
    print(f"You entered the integer: {setNumberStart} and {setNumberEnd}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")



def primeNumberList(setNumberStart, setNumberEnd):
    if setNumberStart < 1 or setNumberEnd < 1:
        return False
    for divisor in range(setNumberStart, setNumberEnd + 1):
        if setNumberStart % divisor == 0:
            return False  # Found a divisor, so it's not prime
    return True

if setNumberStart > setNumberEnd:
    print("Start can't be bigger than End!") 
elif primeNumberList(setNumberStart, setNumberEnd):
    print(f"{setNumberStart}, its a prime number.")