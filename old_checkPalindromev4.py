def test(word2):
    print(word2)
    lenOfOriginalWord = len(word2)
    remainder = 1
    if lenOfOriginalWord % 2 == 0:
        remainder = 0
    while len(word2) != remainder:
        firstCharacter = word2[0]
        lastCharacter = word2[len(word2) - 1]
        if firstCharacter != lastCharacter:
            word2 = word2[1 : len(word2) - 1]
    print(word2)


    #return "test function worked"

def checkPalindrome(word):
    word = word.lower()
    word = word.replace(' ', '')
    originalWord = word
    lenOfOriginalWord = len(word)
    if lenOfOriginalWord == 0:
        return "Not Palindrome"

    remainder = 1
    if lenOfOriginalWord % 2 == 0:
        remainder = 0
    while len(word) != remainder:
        firstCharacter = word[0]
        lastCharacter = word[len(word) - 1]
        if firstCharacter != lastCharacter:
            test(originalWord)
            return "partial Palindrome above"
        word = word[1 : len(word) - 1]
    return "Palindrome"

print(checkPalindrome("Anna"))
print(checkPalindrome("bob"))
print(checkPalindrome("boxb"))
print(checkPalindrome(""))
print(checkPalindrome("abcdefgedcba"))
