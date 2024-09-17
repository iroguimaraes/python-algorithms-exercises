inputNumberStart = input("Write a start number: ")
inputNumberEnd = input("Write a end number: ")


try:
    setNumberStart = int(inputNumberStart)
    setNumberEnd = int(inputNumberEnd)
    print(f"You entered the integer: {setNumberStart} and {setNumberEnd}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")


def primeNumberList(start, end):
    primes = []
    for num in range(max(2, start), end + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

if setNumberStart > setNumberEnd:
    print("Start can't be bigger than End!") 
primeNumbers = primeNumberList(setNumberStart, setNumberEnd)
print(f"{primeNumbers}, its/are prime number.")