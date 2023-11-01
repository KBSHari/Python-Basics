#Find the maximum and minimum elements in a tuple.
import json

my_tuple = (15, 8, 25, 36, 42, 10)

print(max(my_tuple))
print(min(my_tuple))

#Find the intersection and union of two sets.
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

print(set1.intersection(set2))
print(set1.union(set2))

#Remove duplicate elements from a list.
my_list = [1, 2, 2, 3, 4, 4, 5]
my=set(my_list)
print(my)

#Convert to Dict JSON Response and Print and Booking Id AND checkin and Checkout Data

my_data={"bookingid": 2384,
"booking": {"firstname": "PRAMOD","lastname": "Dutta","totalprice": 432,"depositpaid": False,
"bookingdates": {"checkin": "2022-01-01","checkout": "2022-01-01"
},"additionalneeds": "Lunch"
}
}

con_js=json.dumps(my_data,indent=1)

dt=json.loads(con_js)
print(dt["bookingid"])
print(dt["booking"]["bookingdates"]["checkin"])
print(dt["booking"]["bookingdates"]["checkout"])


#Remove a key-value pair from the dictionary.
my_data.pop("bookingid")
print(my_data)
