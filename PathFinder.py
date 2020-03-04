from Path import Path
from Node import Node
from Graph import Graph
from Vector import Vector


class PathFinder:
    """
    finds all paths from one node in a graph to another node

    """

    def __init__(self, from_node, to_node):
        self.from_node = from_node
        self.to_node = to_node
        self.paths = []

    """
    starts the algorithm to find all paths
    all paths are saved in self.paths
    """
    def start(self):
        pass

    """
    _dfs() is intern called to find all paths from one node to another
    """
    def _dfs(self):
        pass
