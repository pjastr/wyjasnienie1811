#  https://peps.python.org/pep-0526/#class-and-instance-variable-annotations

from typing import ClassVar


class Point:
    name: ClassVar[str] = "W"
    name2: str

    def __init__(self, a, b):
        self.x = a
        self.y = b

    def move(self, mx, my):
        self.x += mx
        self.y += my


print(Point.name)
print(Point.name2)
