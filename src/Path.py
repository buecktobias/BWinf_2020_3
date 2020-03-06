import dataclasses
from typing import Set

from src.Node import Node


@dataclasses.dataclass
class Path:
    length: float
    amount_turnoffs: int
    nodes: Set[Node]

    def __copy__(self):
        return Path(length=self.length, amount_turnoffs=self.amount_turnoffs, nodes=self.nodes)
