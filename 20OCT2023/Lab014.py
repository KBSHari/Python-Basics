#Palindrome Checker:
#Create a function that checks if a given string is a palindrome
# (reads the same forwards and backward). 121


def palindrome(check,reverse):
    if check.lower() == reverse.lower():
        print(reverse, "-->Your word is palindrome")
    else:
        print(reverse, "-->Your word is not palindrome")

check=input("Enter the word to check Palindrome or not\n ")
reverse=check[::-1]

palindrome(check,reverse)




