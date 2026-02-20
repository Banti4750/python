# class Point:
#     def draw(self):
#         print("draw")

#     def move(self):
#         print("move")

# point1 = Point()
# point1.x = 10
# point1.y = 20
# print(point1.x)
# point1.draw()
# point1.move()

# point2 = Point()
# print(point2.x) # this will raise an error because x is not defined for point2


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def draw(self):
#         print("draw")

#     def move(self):
#         print("move")

# point1 = Point(10, 20)
# point1.x = 30
# print(point1.x)

# exrecise
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"{self.name} is talking")

person1 = Person("John")
print(person1.name)
person1.talk()