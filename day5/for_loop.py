# for item in "python":
#     print(item)

# for item in range(5):
#     print(item)


# for item in range(5 , 100 , 10):
#     print(item)


# prices = [10, 20, 30, 40, 50]

# total = 0
# for price in prices:
#     total += price

# print(f"Total: {total}")


#  nested loop
# for x in range(4):
#     for y in range(4):
#         print(f"({x}  , {y})")


# f shape task
rows = 5
cols = 5

for i in range(rows):
    for j in range(cols):
        if j == 0 or i == 0 or (i == 2 and j < cols - 1):
            print("X", end="")
        else:
            print(" ", end="")
    print()



