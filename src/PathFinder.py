import copy

from src.Node import Node
from src.Path import Path
from src.Graph import Graph


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
    def _start(self):
        pass

    """
    _dfs() is intern called to find all paths from one node to another
    """
    def _dfs(self,
             current_node: Node,
             last_node: Node,
             path: Path,
             ):
        path.nodes.add(current_node)
        for node in current_node.get_neighbours():
            if node == self.to_node:
                self.paths.append(path)
                break
            if node in path.nodes:
                continue

            new_path = copy.copy(path)
            new_path.length += Graph.distance(current_node, node)
            new_path.amount_turnoffs += Graph.is_turnoff(last_node, current_node, node)
            self._dfs(node, current_node, new_path)
    """
    returns all paths
    """
    def get_paths(self):
        self._start()
        return self.paths
