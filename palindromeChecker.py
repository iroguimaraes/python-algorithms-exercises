word = input(str("Digite a palavra: "))
fullWord = []
invertedWord = []
letter = 0
wordCounter = 0
isPalindrome = 0
wordLength = len(word)

cleanWord = word.replace(" ", "").lower() #removes spaces and lowercase

while letter < wordLength:
    invertedLetter = cleanWord[letter]
    fullWord.insert(letter, invertedLetter)
    letter += 1

invertedWord = fullWord[::-1]
print("fullWord", fullWord)
print("invertedWord", invertedWord)

while wordCounter < wordLength:
    if invertedWord[wordCounter] != fullWord[wordCounter]:
        isPalindrome += 1
    wordCounter += 1


if isPalindrome >= 1:
    print(f"'{cleanWord}' ISN'T Palindrome")
elif isPalindrome < 1:
    print(f"'{cleanWord}' IS Palindrome")