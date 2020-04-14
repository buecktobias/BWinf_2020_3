from src.graph.Node import Node
from src.math.Vector import Vector


class Graph:
    """
    undirected graph

    """
    
    instance = None
    
    @classmethod
    def get_instance(cls):
        return cls.instance
    
    def __init__(self):
        self.nodes = set()
        self.__class__.instance = self
        
    def add_node(self, node):
        self.nodes.add(node)

    @staticmethod
    def distance(node1: Node, node2: Node):
        return node1.distance_to(node2)

    @staticmethod
    def is_turnoff(node1: Node, node2: Node, node3: Node):
        first_edge: Vector = node1.position.way_to(node2.position)
        second_edge: Vector = node2.position.way_to(node3.position)
        return not first_edge.same_direction(second_edge)

    def add_edge(self, node1, node2):
        self.add_node(node1)
        self.add_node(node2)
        node1.add_neighbour(node2)
        node2.add_neighbour(node1)


