from typing import Dict, Tuple

from src.graph import Graph, Node
from src.settings import Settings
import os


def coordinates(cord_string):
    x, y = cord_string.replace("(", "").replace(")", "").split(",")
    x = int(x)
    y = int(y)
    return x, y


class Input:
    def __init__(self):
        self.input_folder = os.path.join(Settings.get_PROJECT_DIR(), "input/")
        self.graph = Graph.Graph()

    def create_graph(self, file_name):
        lines = self.read_file(file_name)
        start_node_cords = coordinates(lines[1])
        target_node_cords = coordinates(lines[2])

        nodes_dict: Dict[Tuple[int, int], Node] = {}

        for i in range(3, len(lines)):
            line = lines[i]
            if len(line.split(" ")) > 1:
                from_node_cords, to_node_cords = line.split(" ", 1)
                from_node_cords = coordinates(from_node_cords)
                to_node_cords = coordinates(to_node_cords)
                if from_node_cords in nodes_dict:
                    from_node = nodes_dict[from_node_cords]
                else:
                    from_node = Node.Node(*from_node_cords)

                if to_node_cords in nodes_dict:
                    to_node = nodes_dict[to_node_cords]
                else:
                    to_node = Node.Node(*to_node_cords)
                nodes_dict[from_node_cords] = from_node
                nodes_dict[to_node_cords] = to_node
                self.graph.add_edge(from_node, to_node)
            else:
                raise ValueError("Die Zeile ist falsch lol!")

        start_node = nodes_dict[start_node_cords]
        target_node = nodes_dict[target_node_cords]
        return start_node, target_node

    def read_file(self, file_name):
        path = os.path.join(self.input_folder, "abbiegen" + file_name + ".txt")
        with open(path, "r") as input_file:
            text = input_file.read()

        lines = text.split("\n")
        return lines


if __name__ == '__main__':
    print(coordinates("(2,33333)"))