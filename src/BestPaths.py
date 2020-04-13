from typing import List, Dict

from src.Graph import Graph
from src.Node import Node
from src.Path import Path
from src.Settings import INFINITY


class BestPaths:

    def __init__(self, from_node: Node, to_node: Node, max_path_length: float, max_turnoffs: int):
        self.from_node = from_node
        self.to_node = to_node

        self.max_turnoffs = max_turnoffs
        self.max_path_length = max_path_length

        graph = Graph.get_instance()
        nodes = list(graph.nodes)

        """
        best_path_nodes safes the best paths to nodes, there can be multiple.
        Since if a path has less abbiegungen, but is longer it could possibly be better.
        """

        self.best_paths_nodes: Dict[Node, List[Path]] = {node: [Path(INFINITY, INFINITY, [])] for node in nodes}
        self.best_paths_nodes[from_node] = [Path(0, 0, [from_node])]

    def add_best_paths_to(self, node: Node, paths: List[Path]):
        if isinstance(node, Node):
            current_paths = self.get_best_paths_to(node)
            combined = current_paths + paths
            self.set_best_paths_to(node, combined)
        else:
            raise ValueError("node must be of type Node")

    def set_best_paths_to(self, node: Node, paths: List[Path]):
        self.best_paths_nodes[node] = paths

    def get_best_paths_to(self, to_node: Node) -> List[Path]:
        return self.best_paths_nodes[to_node]

    """
    Gets the paths with the least turn offs, which path length is lower than @param length_bound
    """

    def get_path_least_turn_offs(self, node: Node, length_bound: float) -> Path:
        paths: List[Path] = self.get_best_paths_to(node)
        path_least_turnoffs = Path.get_path_least_turn_offs_shorter_than(paths, length_bound)
        return path_least_turnoffs

    """
    Removinng unusable paths, they are longer and have more Abbiegungen from a node in the dict.
    """

    def remove_unusable_paths(self, node) -> List[Path]:
        paths = self.get_best_paths_to(node)
        useable_paths = Path.filter_paths_unuseable(paths, self.max_turnoffs, self.max_path_length, self.to_node)
        self.set_best_paths_to(node, useable_paths)
        return list(set(paths) - set(useable_paths))
    """
    Adds new paths to a node and returns a list of paths which are an improvement
    """

    def new_paths_to_node(self, new_paths: List[Path], node: Node) -> List[Path]:  # TODO or set ?
        self.add_best_paths_to(node, new_paths)
        return self.remove_unusable_paths(node)
