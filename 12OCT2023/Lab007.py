"""Task #2"""

"""Write a Python program to calculate the area of a circle given its radius using the formula
area=π×r^2 ( Take pie as 3.14)"""

Pi=3.14
r=float(2)
a=Pi*(r*r)
print(a)

"""Create a program that takes two numbers as input and prints whether the first number is greater than,
less than, or equal to the second number."""

a=input("Enter First Number:\t")
b=input("Enter second Number:\t")

if(a>=b or a<=b):
    print(a)
else:
    print("Second number is greater number")

#Use the ternary operator to find the maximum of three numbers entered by the user.

a=input("Enter First Number:\t")
b=input("Enter second Number:\t")
c=input("Enter Third Number:\t")

mm= a if (a>b and a>c) else (b if b>c else c)
print(mm)

#Develop a Python script that calculates the square and cube of a given number.

s=float(input("Enter sqaure number: "))
print("Square value of s: ",s*s)
print("Cube value of s: ",s*s*s)


