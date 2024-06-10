#Classes
class Point:
    def move(self):
        print('move')
    def draw(self):
        print('draw')


print(type(Point))
point1 = Point()
point1.draw()
point1.x = 10
point1.y = 20
print(point1.y)

point2 = Point()
point2.x = 1
point2.y = 3
print(point2.x)




