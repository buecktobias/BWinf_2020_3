from src.paths.Path import Path
from src.graph.Node import Node


class Item:
    def __init__(self, path: Path, target_node):
        self.target_node = target_node
        self.path = path

    def __lt__(self, other):
        self_best_possible_turnoffs = self.path.best_possible_turnoffs(self.target_node)
        other_best_possible_turnoffs = other.path.best_possible_turnoffs(self.target_node)
        if self_best_possible_turnoffs < other_best_possible_turnoffs:
            return True
        elif self_best_possible_turnoffs == other_best_possible_turnoffs:
            return self.path.length < other.path.length
        else:
            return False


if __name__ == '__main__':
    node = Node(0, 0)
    p1 = Item(Path(9, 3, []), node)
    p2 = Item(Path(10, 3, []), node)
    print(p1 < p2)
