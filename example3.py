from typing import ClassVar


class Point:
    name: ClassVar[str] = "W"
    x: float
    y: float

    def __init__(self, a: float, b: float) -> None:
        self.x = a
        self.y = b

    def move(self, mx: float, my: float) -> None:
        self.x += mx
        self.y += my


p1 = Point(2, 2)
print(p1.name)
p1.name = "A"
print(p1.name)
print(p1.__class__.name)
