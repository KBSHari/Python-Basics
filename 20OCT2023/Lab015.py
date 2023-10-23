"""Sum of Digits: Create a function that calculates the sum of the digits of a positive integer.
n = 12345
sum = 15
n = 123
sum = 6"""


def addition(digits):
    lt = []
    for i in digits:
        a = int(i)
        lt.append(a)
    print(sum(lt))


numbers = input("Enter your n numbers value and provide list of input: ")
digits=numbers.split()

addition(digits)







