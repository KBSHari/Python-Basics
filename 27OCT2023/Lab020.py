lt=[1,12,2,24,15,45,3]

#Write a Python program to find the largest number in a list.
print("Max value in list: ",max(lt))

#Write a Python program to find the smallest number in a list.
print("Min value in list: ",min(lt))

#Write a Python program to sum all numbers in a list.
print("Sum of list: ",sum(lt))

#Write a Python program to multiply all numbers in a list.
a=1
for i in lt:
    a=a*i
print("Multiply of list: ",a)

"""Write a Python program to count the number of strings in a list
where the string length is 2 or more and the first and last character are the same."""


lt1=["test","sun","comic","QA","window"]

for i in lt1:
    if len(i)>=2:
        if i[0]==i[-1]:
            print(f"{i} length is:",len(i))


