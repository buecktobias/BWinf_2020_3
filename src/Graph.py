from src.Node import Node
from src.Vector import Vector
from src.PathFinder import PathFinder


class Graph:
    """
    undirected graph

    """

    def __init__(self, node):
        self.root_node = node

    @staticmethod
    def is_turnoff(node1: Node, node2: Node, node3: Node):
        first_edge: Vector = node1.pos.way_to(node2.pos)
        second_edge: Vector = node2.pos.way_to(node3.pos)
        return not first_edge.same_direction(second_edge)

    @staticmethod
    def add_edge(node1, node2):
        node1.add_neighbour(node2)
        node2.add_neighbour(node1)

    @staticmethod
    def get_all_paths(from_node, to_node):
        return PathFinder(from_node, to_node).get_paths()


