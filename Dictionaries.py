#Author: Tithy
#Date: 2026-07-12
#Description: Dictionaries in Python.
#Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered*, changeable and does not allow duplicates.

# Name: John
# Email: john@gmail.com

customer = {
    "name": "John",
    "age": 30,
    "is_verified": True
}
# print(customer["birthdate"]) #Will throw an error because birthdate key isn't present it the dictionary.
# print(customer["Name"]) #Will also throw an error due to case sensitivity.
print(customer["name"])

#Absent key will return None instead of throwing an error.
print(customer.get("birthdate"))
#Absent key will return default value instead of showing none.
print(customer.get("birthdate", "Not present"))

#Update a value in the ditionary.
customer["name"] = "Jack"
print(customer["name"])

#Add a new key in dictionary.
customer["birthdate"] = "Jan 1, 1999"
print(customer.get("birthdate"))
