"""
✅ Create a Function with a Parameter which can do x^y
"""
x=int(input("Enter x value: "))
y=int(input("Enter y value: "))

def power(x,y):
    z=x**y
    return z

c=power(x,y)
print(c)

#✅ Create a Lambda expression to triple power 2**3 a number

LE=lambda x,y: x**3
print(LE(x,y))