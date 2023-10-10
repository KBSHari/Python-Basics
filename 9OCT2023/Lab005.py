"""Create a program ,take 5 numbers from the user,add 1-2 duplicate
and print the non-duplicate numbers"""
c = []
for i in range(1,6):
    a=input("Enter your number:\t")
    c.append(a)
d=set(c)
print(d)
