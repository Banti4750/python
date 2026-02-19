person = {
    "name" : "John",
    "age" : 30,
    "city" : "New York"
}

print(person["name"])
print(person.get("age"))
print(person.keys())
print(person.values())
print(person.items())
print("name" in person)
print("country" in person)
print(len(person))
# print(person["country"]) # KeyError
print(person.get("country")) # None
print(person.get("country" , "Not Found")) # Not Found
print(person.setdefault("country" , "USA")) # USA
print(person)