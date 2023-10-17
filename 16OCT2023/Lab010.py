"""Write a program that classifies a triangle based on its side lengths.
Given three input values representing the lengths of the sides,

determine if the triangle is equilateral (all sides are equal),
isosceles (exactly two sides are equal), or scalene (no sides are equal).
Use an if-else statement to classify the triangle.

3 Input
side 1, side 2 and side 3
output - Eq, Iso, Scalene -

Eq. = side 1 == side 2 = side 3"""

A=int(input("Enter First Side: "))
B=int(input("Enter Second Side: "))
C=int(input("Enter Third Side: "))

if A==B and A==C:
    print("Equilateral")
elif A==B or A==C or B==C:
    print("Isosceles")
else:
    print("Scalene")

