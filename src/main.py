from src.graph.Graph import Graph
from src.graph.Node import Node
from src.IO.UserInterface import UserInterface


def create_test_graph():
    n1 = Node(0, 0)
    n2 = Node(0, 1)
    n3 = Node(1, 1)
    n4 = Node(0, 2)
    n5 = Node(1, 2)
    n6 = Node(0, 3)
    n7 = Node(1, 3)

    start_node: Node = n1
    end_node: Node = n7
    graph = Graph()
    graph.add_edge(n1, n2)
    graph.add_edge(n2, n3)
    graph.add_edge(n2, n4)
    graph.add_edge(n4, n6)
    graph.add_edge(n2, n5)
    graph.add_edge(n3, n5)
    graph.add_edge(n5, n7)
    graph.add_edge(n6, n7)

    return start_node, end_node


if __name__ == '__main__':
    start_node, end_node = create_test_graph()
    ui = UserInterface(start_node, end_node)
