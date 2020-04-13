# IMPORTS
import copy
from typing import List

# PROJECT IMPORTS

from src.Node import Node
from src.Path import Path
from src.BestPaths import BestPaths
from src.Settings import INFINITY


class PathFinder:

    def __init__(self, from_node, to_node):
        self.max_path_length = INFINITY
        self.max_turnoffs = INFINITY
        self.from_node = from_node
        self.to_node = to_node

        self.best_paths = BestPaths(from_node, to_node, self.max_path_length, self.max_turnoffs)

    def start(self):
        self._dfs(self.from_node)

    """
    _dfs() is intern called to selffind all paths from one node to another
    """

    def _dfs(self, current_node: Node, paths: List[Path] = None):
        if paths is not None:
           new_paths_to_current_node = list(set(paths))
        else:
            new_paths_to_current_node: List[Path] = self.best_paths.get_best_paths_to(current_node)

        neighbours = current_node.get_neighbours()

        # TODO sort neighbours by relevance
        for neighbour in neighbours:
            new_paths = []
            for path in new_paths_to_current_node:
                if not path.has_node(neighbour):
                    c_path = copy.copy(path)
                    c_path.add_node(neighbour)
                    new_paths.append(c_path)


            # TODO error
            new_useable_paths: List[Path] = self.best_paths.new_paths_to_node(new_paths, neighbour)
            if len(new_useable_paths) > 0:
                self._dfs(neighbour, new_useable_paths)

    def get_path_least_turn_offs(self, max_percentage_extension: int):
        factor: float = max_percentage_extension / 100
        best_paths_to_target_node: List[Path] = self.best_paths.get_best_paths_to(self.to_node)
        shortest = Path.get_length_of_shortest_path(best_paths_to_target_node)

        max_path_length: float = shortest * (factor + 1)

        best_path = Path.get_path_least_turn_offs_shorter_than(best_paths_to_target_node, max_path_length)
        return best_path
