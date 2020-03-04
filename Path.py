import dataclasses
from typing import List

from Node import Node


@dataclasses.dataclass
class Path:
    length: float
    amount_turnoffs: int
    nodes: List[Node]
