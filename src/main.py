if __name__ == '__main__':
    from src.Graph import Graph
    from src.Node import Node

    num = 2
    num += False
    print(num)

    n1 = Node(0, 0)
    n2 = Node(0, 1)
    n3 = Node(1, 1)
    n4 = Node(0, 2)
    n5 = Node(1, 2)
    n6 = Node(0, 3)
    n7 = Node(1, 3)

    start_node = n1
    end_node = n7

    Graph.add_edge(n1, n2)
    Graph.add_edge(n2, n3)
    Graph.add_edge(n2, n4)
    Graph.add_edge(n4, n6)
    Graph.add_edge(n2, n5)
    Graph.add_edge(n3, n5)
    Graph.add_edge(n5, n7)

    print(Graph.is_turnoff(n1, n2, n5))


