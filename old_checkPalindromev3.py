def checkPalindrome(word):
    print('here')
    word = word.lower()
    print(word)
    word = word.replace(' ', '')
    lenOfOriginalWord = len(word)
    if lenOfOriginalWord == 0:
        print('Not Palindrome')
    remainder = 1
    if lenOfOriginalWord % 2 == 0:
        remainder = 0
    while len(word) != remainder:
        firstCharacter = word[0]
        lastCharacter = word[len(word) - 1]
        if firstCharacter != lastCharacter:
            print("Not Palindrome")
        word = word[1 : len(word) - 1]
    print("Palindrome")

word1 = input('Enter the word to check: ')
checkPalindrome(word1)
