from math import sqrt
import copy
from typing import Any, Callable, Union


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):
        return self.way_to(other).length()

    def way_to(self, other_vec):
        return other_vec - self

    def __sub__(self, other):
        c_self = copy.copy(self)
        c_self.x -= other.x
        c_self.y -= other.y
        return c_self

    def __copy__(self):
        return Vector(self.x, self.y)

    def for_each(self, func):
        self.x = func(self.x)
        self.y = func(self.y)

    def length(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def unit_vector(self):
        copy_self = copy.copy(self)
        copy_self.for_each(lambda el: el / self.length())
        return copy_self

    def same_direction(self, other):
        round_2 = lambda el: round(el, 2)
        c_self = copy.copy(self)
        c_other = copy.copy(other)
        c_self.for_each(round_2)
        c_other.for_each(round_2)

        return c_self.unit_vector() == c_other.unit_vector()

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"{self.x}, {self.y}"


if __name__ == '__main__':
    vec = Vector(4, 4)
    vec2 = Vector(9, 8)
    print(vec)
    print(vec.way_to(vec2))
