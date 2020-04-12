import dataclasses
from typing import List, Tuple
from src.Graph import Graph
from src.Node import Node


@dataclasses.dataclass
class Path:
    length: float
    amount_turnoffs: int
    nodes: List[Node]

    def best_possible_turnoffs(self, to_node: Node):
        nodes = self.get_last_two_nodes()
        is_turnoff = Graph.is_turnoff(*nodes, to_node)
        if is_turnoff:
            return self.amount_turnoffs + 1
        else:
            return self.amount_turnoffs

    def best_possible_length(self, to_node: Node):
        distance_to_target_node = self.get_last_node().distance_to(to_node)
        return self.length + distance_to_target_node

    @staticmethod
    def filter_paths_unuseable(paths: List, maximum_turnoffs: int, maximum_length: float, to_node: Node):
        paths_possible_useable = list(filter(lambda path: path.best_possible_length(to_node) <= maximum_length and path.best_possible_turnoffs(to_node) <= maximum_turnoffs, paths))
        useable_paths = list(filter(lambda path: not all([other_path.  for other_path in paths_possible_useable ])))
        # TODO  ?? was geht ab haha

    @staticmethod
    def get_paths_shorter_than(paths: List, length: float) -> List:
        return list(filter(lambda path: path.length < length, paths))

    @staticmethod
    def get_path_least_turn_offs_shorter_than(paths: List, max_length: float):
        shorter_paths: List = Path.get_paths_shorter_than(paths, max_length)
        path_least_turnoffs = Path.get_path_least_turnoffs(shorter_paths)
        return path_least_turnoffs

    @staticmethod
    def get_length_of_shortest_path(paths: List) -> float:
        return Path.get_shortest_path(paths).length

    @staticmethod
    def get_path_least_turnoffs(paths: List):
        return min(paths, key=lambda path: path.amount_turnoffs)

    @staticmethod
    def get_shortest_path(paths: List):  # list of Paths -> Path
        return min(paths, key=lambda path: path.length)

    def has_node(self, node: Node):
        # TODO set ? faster but more space
        return node in self.nodes

    def get_last_two_nodes(self) -> Tuple[Node, Node]:
        return self.nodes[-2], self.nodes[-1]

    def get_last_node(self) -> Node:
        return self.nodes[-1]

    def add_node(self):
        pass

    def _add_node(self, node: Node):
        self.nodes.append(node)

    def __copy__(self):
        return Path(length=self.length, amount_turnoffs=self.amount_turnoffs, nodes=self.nodes[:])
