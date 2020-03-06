import dataclasses
from typing import Set, List

from src.Node import Node


@dataclasses.dataclass
class Path:
    length: float
    amount_turnoffs: int
    nodes: List[Node]

    def add_node(self, node):
        self.nodes.append(node)

    def __copy__(self):
        return Path(length=self.length, amount_turnoffs=self.amount_turnoffs, nodes=self.nodes[:])
