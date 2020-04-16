import dataclasses
from typing import List, Tuple, Optional
from src.graph.Graph import Graph
from src.graph.Node import Node


@dataclasses.dataclass
class Path:
    length: float
    amount_turnoffs: int
    nodes: List[Node]

    def best_possible_turnoffs(self, to_node: Node):
        nodes = self.get_last_two_nodes()
        if nodes is not None:
            is_turnoff = Graph.is_turnoff(*nodes, to_node)
            if is_turnoff:
                return self.amount_turnoffs + 1
            else:
                return self.amount_turnoffs
        else:
            return self.amount_turnoffs

    def best_possible_length(self, to_node: Node):
        if self.get_last_node() is not None:
            distance_to_target_node = self.get_last_node().distance_to(to_node)
            return self.length + distance_to_target_node
        else:
            return self.length

    @staticmethod
    def filter_paths(path, paths_possible_useable):
        # TODO test
        # nicht alle sollen kürzere Wege haben und weniger Abbiegungen
        return not any([other_path.length < path.length and other_path.amount_turnoffs < path.amount_turnoffs for other_path in paths_possible_useable])

    @staticmethod
    def filter_paths_unuseable(paths: List, maximum_turnoffs: int, maximum_length: float, to_node: Node):
        paths_possible_useable = list(filter(lambda path: path.best_possible_length(to_node) <= maximum_length and path.best_possible_turnoffs(to_node) <= maximum_turnoffs, paths))

        # Alle Wege welche länger und mehr Abbiegungen haben, müssen rausgekickt werden
        useable_paths = list(filter(lambda path: Path.filter_paths(path, paths_possible_useable), paths_possible_useable))
        return useable_paths

    @staticmethod
    def get_paths_shorter_than(paths: List, length: float) -> List:
        return list(filter(lambda path: path.length < length, paths))

    @staticmethod
    def get_path_least_turn_offs_shorter_than(paths: list, max_length: float):
        shorter_paths: list = Path.get_paths_shorter_than(paths, max_length)
        path_least_turnoffs: Path = Path.get_path_least_turnoffs(shorter_paths)
        return path_least_turnoffs

    @staticmethod
    def get_length_of_shortest_path(paths: List) -> float:
        shortest_path = Path.get_shortest_path(paths)
        if shortest_path is not None:
            return shortest_path.length

    @staticmethod
    def get_path_least_turnoffs(paths: list):
        return min(paths, key=lambda path: path.amount_turnoffs)

    @staticmethod
    def get_shortest_path(paths: List):  # list of Paths -> Path
        if len(paths) > 0:
            return min(paths, key=lambda path: path.length)
        else:
            return None

    def has_node(self, node: Node):
        # TODO set ? faster but more space
        return node in self.nodes

    def get_last_two_nodes(self) -> Optional[Tuple[Node, Node]]:  # TODO errors no nodes
        if len(self.nodes) >= 2:
            return self.nodes[-2], self.nodes[-1]
        else:
            return None

    def get_last_node(self) -> Optional[Node]:  # TODO errors no nodes
        if len(self.nodes) >= 1:
            return self.nodes[-1]
        else:
            return None

    def add_node(self, node: Node):
        nodes_before = self.get_last_two_nodes()
        if nodes_before is not None:
            if Graph.is_turnoff(*nodes_before, node):
                self.amount_turnoffs += 1
        last_node = self.get_last_node()
        if last_node is not None:
            self.length += last_node.distance_to(node)
        self._add_node(node)

    def _add_node(self, node: Node):
        self.nodes.append(node)

    def __hash__(self):
        return hash((self.length, tuple(self.nodes), self.amount_turnoffs))

    def __copy__(self):
        return Path(length=self.length, amount_turnoffs=self.amount_turnoffs, nodes=self.nodes[:])


if __name__ == '__main__':
    test_paths = [Path(3, 0, []), Path(2, 7, []), Path(5, 5, []), Path(10, 10, [])]
    useable_paqths = Path.filter_paths_unuseable(test_paths, 999, 999, Node(10, 10))
    print(useable_paqths)
