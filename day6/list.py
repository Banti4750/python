# names = ["banti" , "sam" , "suraj"]
# print(names)
# print(names[1])
# print(names[0:2])


# largest number in list
numbers = [12 , 45 , 67 ,44]

# res = 0
# for items in numbers:
#     if items > res:
#         res = items

# print(res)

# list method
# numbers.append(111)
numbers.insert(0 , 12)
# numbers.remove(12)
# numbers.clear()
# numbers.pop()
# print(numbers.index(12))
# print(12 in numbers )
# print(numbers.count(12))
# numbers.sort()
# numbers.reverse()
numbers2 = numbers.copy()
# print(numbers2)


# remove dupliate from list

numbers = [12 , 12 , 34 , 56 , 1 , 3 ,1 ]
uniques = []
for items in numbers:
    if items not in uniques :
        uniques.append(items)

print(uniques)