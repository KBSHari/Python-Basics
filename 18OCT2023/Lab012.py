"""Task 2
Example using break to exit a loop when i == 51 while printing the values from 1 to 100"""

for i in range(1,101):
    print(i,end=" ")
    if i==51:
        break
print("\n")
print("Loop stoped at given condition")