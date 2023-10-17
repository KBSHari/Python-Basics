"""Create a program that determines whether a given year is a leap year.

A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
Use an if-else statement to make this determination.

How to know if it is a Leap Year:
Leap Years are any year that can be exactly divided by 4 (such as 2016, 2020, 2024, etc)
except if it can be exactly divided by 100, then it isn't (such as 2100, 2200, etc)
except if it can be exactly divided by 400, then it is (such as 2000, 2400)

Input = 2024,Output = Leap year"""

year=2016

if year%4==0 and year%100!=0:
    print("Leap year")
elif year%400==0 and year%100==0:
    print("Leap year")
else:
    print("Not Leap Year")
