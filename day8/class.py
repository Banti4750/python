class Point:
    def draw(self):
        print("draw")

    def move(self):
        print("move")

point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()
point1.move()

point2 = Point()
print(point2.x) # this will raise an error because x is not defined for point2