#Task 3 :List the all the functions avaiable for the String Data Type.

#Format string+integer
b=25
print("Happy Start {}".format(b))
print(f"Happy Start {b}")

#Split the based on value
a="Welcome Tester"
print(a.split("t"))

# iterable and joins them into one string.
j="join"
c="+-"
print(j.join(c))

#strip Used to trim whitespaces from the string object.
d="   John"
print(d.strip())

#convert a string to uppercase
e="automation"
print(e.upper())

#convert a string to lowercase
fe="TESTER WITH WAITER"
print(fe.lower())

#replace() function is used to create a new string by replacing some parts of another string.
g="Report"
print(g.replace("po","A"))

# method is used to find the index of a substring
h="Maxi"
print(h.find("x"))

#replace & translate works similar
#function is used to encode the string
i="setmax with jet"
print(i.encode())

# function returns the number of occurrences of a substring
j="testwaste"
print(j.count("t"))

#function returns True if the string starts with the given prefix
k="Maxlight"
print(k.startswith("M"))

#function returns True if the string starts with the given sufix
l="Maxwhite"
print(l.endswith("e"))

#function returns the capitalized version of the string first letter.
m="rest"
print(m.capitalize())

#function returns a centered string of specified size
n="minimumvalue"
print(n.center(50))

#casefold() function returns string in lower case like .lower() function

#function returns a new string with tab size characters
o="New\tmember\t"
print(o.expandtabs(50))

# function returns the lowest index
p="loweststring"
print(p.index("s"))

#len
q="timer"
print(len(q))

#Swaps cases conver lower to upper & upper to lower
r="TRwaste MRtime RTwine"
print(r.swapcase())

#string is parted into three parts
s="I eat chicken daily"
print(s.partition("chicken"))

#True if all characters in the string are digits
t="12354"
print(t.isdigit())

#