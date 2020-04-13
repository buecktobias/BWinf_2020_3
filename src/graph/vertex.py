from typing import List, Set


class Vertex:
    def __init__(self, position: Position, neighbours=None):
        if neighbours is None:
            neighbours = []
        self.position = position
        self.neighbours: Set[Vertex] = set(neighbours)

    def add_neighbour(self, neighbour):
        neighbour.neighbours.add(self)
        self.neighbours.add(neighbour)

    def add_neighbours(self, neighbours):
        for neighbour in neighbours:
            self.add_neighbour(neighbour)

    def distance(self, other):
        if other in self.neighbours:
            return 1
        raise ValueError(f"{other} is not a neighbour")

    def __lt__(self, other):
        return 0 < 1

    def __repr__(self):
        return f"{self.position}"

    def __eq__(self, other):
        return self.position == other.position

    def __hash__(self):
        return hash(self.position)
