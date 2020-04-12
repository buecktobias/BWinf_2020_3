import dataclasses
from typing import List, Tuple

from src.Node import Node


@dataclasses.dataclass
class Path:
    length: float
    amount_turnoffs: int
    nodes: List[Node]
    # TODO set ?

    @staticmethod
    def filter_paths_unuseable(paths: List, maximum_turnoffs, maximum_length):
        # TODO filter all paths which have more than maximum_turnoffs, maximum_length
        # TODO sort elements by turnoffs, or insert new faster ?? binary search v * log(n) or sorting: v+n * log(v+n)...
        # TODO kicking out all paths which are longer and have more turnoffs !!! also filter ???
        # for loop save most least turnoffs least length pair ??????
        pass


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
