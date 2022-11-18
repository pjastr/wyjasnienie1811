class Point:
    name = "W"

    def __init__(self, a, b):
        self.x = a
        self.y = b

    def move(self, mx, my):
        self.x += mx
        self.y += my


p1 = Point(2, 2)
print(p1.name)
p1.name = "A"
print(p1.name)
print(p1.__class__.name)

