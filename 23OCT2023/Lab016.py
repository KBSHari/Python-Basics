"""Task 1-✅ Count vowels and consonants in a String
aeiou
input = pramod
vol = 2"""

user=input("Enter your word to find count of vowels\n")

vowels="aeiou"
count=0

for i in vowels:
    for j in user:
        if i==j:
            count=count+1

print(f"Your word vowels count: {count}")


