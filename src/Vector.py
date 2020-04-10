from math import sqrt
import copy


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):
        return self.way_to(other).length()

    def way_to(self, other_vec):
        return other_vec - self

    def for_each(self, func):
        self.x = func(self.x)
        self.y = func(self.y)

    def length(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def unit_vector(self):
        copy_self = copy.copy(self)
        if self.length() != 0:
            copy_self.for_each(lambda el: el / self.length())
        else:
            copy_self.for_each(lambda x: 0)
        return copy_self

    def same_direction(self, other):
        round_2 = lambda el: round(el, 2)

        c_self = copy.copy(self)
        c_other = copy.copy(other)
        c_self.for_each(round_2)
        c_other.for_each(round_2)

        return c_self.unit_vector() == c_other.unit_vector()

    def __sub__(self, other):
        c_self = copy.copy(self)
        c_self.x -= other.x
        c_self.y -= other.y
        return c_self

    def __copy__(self):
        return Vector(self.x, self.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"({self.x}, {self.y})"
