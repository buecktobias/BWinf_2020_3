from src.Vector import Vector


class Node:
    def __init__(self, pos_x, pos_y):
        self.pos = Vector(pos_x, pos_y)
        self._neighbours = set()

    def distance_to(self, node):
        return self.pos.distance_to(node.pos)

    def get_neighbours(self):
        return self._neighbours

    def add_neighbour(self, node):
        self._neighbours.add(node)

    def __repr__(self):
        return str(self.pos)
