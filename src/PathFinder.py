# IMPORTS

from typing import List
import sys

# PROJECT IMPORTS

from src.Node import Node
from src.Path import Path
from src.Graph import Graph

# CONSTANTS

INFINITY = sys.maxsize


"""
Gets the paths with the least turn offs, which path length is lower than
 
"""


def get_path_least_turn_offs(paths: List[Path], length_bound: float) -> Path:
    pass


"""
Removinng unusable paths, they are longer and have more Abbiegungen
"""


def remove_unusable_paths(path1: Path, paths: List[Path]):
    pass


"""
Adds new path to paths, and removes unusables
"""


def new_path_to_node(path1: Path, paths: List[Path]):
    # Adding of path to best paths
    # then filtering of paths if , they are useable
    pass


"""
Checks whether a path to a node, is an improvement, this path makes sense ???
"""


def better_path(path1: Path, paths: List[Path]):
    # checks whether this path makes sense
    pass


class PathFinder:
    """
    finds all paths from one node in a graph to another node

    """

    def __init__(self, from_node, to_node):
        self.from_node = from_node
        self.to_node = to_node
        self.paths = []
        graph = Graph.get_instance()
        nodes = list(graph.nodes)

        """
        best_path_nodes safes the best paths to nodes, there can be multiple.
        Since if a path has less abbiegungen, but is longer it could possibly be better.
        """
        self.best_paths_nodes = {node: [Path(INFINITY, INFINITY, [])] for node in nodes}
        self.best_paths_nodes[from_node] = Path(0, 0, [])

    def get_best_paths_to(self, to_node: Node) -> List[Path]:
        return self.best_paths_nodes[to_node]

    """
    starts the algorithm to find all paths
    all paths are saved in self.paths
    """

    def start(self):
        self._dfs(self.from_node)

    """
    _dfs() is intern called to selffind all paths from one node to another
    """

    def _dfs(self, current_node: Node):
        best_paths_to_current_node: List[Path] = self.get_best_paths_to(current_node)


    def get_path_least_turn_offs(self, max_percentage_extension: int):
        factor: float = max_percentage_extension / 100
        best_paths_to_target_node: List[Path] = self.get_best_paths_to(self.to_node)
        shortest = min(best_paths_to_target_node, key=lambda path: path.length).length

        max_path_length: float = shortest * (factor + 1)

        best_path = get_path_least_turn_offs(self.paths, max_path_length)
        return best_path

    """
    returns all paths
    """

    def get_paths(self):
        if len(self.paths) == 0:
            self.start()
        return self.paths
