def happyBirthday(person):
    print("Happy birthday dear " + person)
    
def main():
    happyBirthday('John')
    happyBirthday('Emily')
    print('In function main')
    userName = input("Enter the name: ")
    happyBirthday(userName)

print('When does this print?')

main()