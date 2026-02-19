# take 1234 and print each digit on a new line.
number = int(input("Enter a number : "))

numbermap = {
    0 : "Zero",
    1 : "One",
    2 : "Two",
    3 : "Three",
    4 : "Four",
    5 : "Five",
    6 : "Six",
    7 : "Seven",
    8 : "Eight",
    9 : "Nine"
}

digits = ""

while number > 0:
    digit = number % 10
    digits+=f" " + numbermap[digit]
    number = number // 10

print(digits)