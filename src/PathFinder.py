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
        self._dfs(self.from_node, self.from_node, Path(0, 0, []))  # division by zero , cause zero-length vector

    """
    _dfs() is intern called to selffind all paths from one node to another
    """
    def _dfs(self,
             current_node: Node,
             last_node: Node,
             path: Path,
             ):
        path.add_node(current_node)
        for node in current_node.get_neighbours():
            if node == self.to_node:
                path.add_node(self.to_node)
                path.length += Graph.distance(current_node, node)
                path.amount_turnoffs += Graph.is_turnoff(last_node, current_node, node)
                self.paths.append(path)
                break
            if node in path.nodes:
                continue

            new_path = copy.copy(path)
            new_path.length += Graph.distance(current_node, node)
            new_path.amount_turnoffs += Graph.is_turnoff(last_node, current_node, node)
            self._dfs(node, current_node, new_path)

    def get_path_least_turn_offs(self, max_percentage_extension: int):
        factor = 1 + max_percentage_extension / 100
        self.paths.sort(key=lambda path: path.length)
        shortest = self.paths[0]
        best_path = sorted(filter(lambda path: path.length / factor <= shortest.length, self.paths), key=lambda path: path.amount_turnoffs)[0]
        return best_path

    """
    returns all paths
    """
    def get_paths(self):
        if len(self.paths) == 0:
            self._start()
        return self.paths
