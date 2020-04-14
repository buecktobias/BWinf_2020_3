from src.math.Vector import Vector


class Node:
    def __init__(self, pos_x, pos_y):
        self.position = Vector(pos_x, pos_y)
        self._neighbours = set()

    def get_position(self):
        return self.position

    def distance_to(self, node):
        return self.position.distance_to(node.position)

    def get_neighbours(self):
        return self._neighbours

    def add_neighbour(self, node):
        self._neighbours.add(node)

    def __hash__(self):
        return hash(self.position)

    def __eq__(self, other):
        return self.position == other.position

    def __repr__(self):
        return str(self.position)
