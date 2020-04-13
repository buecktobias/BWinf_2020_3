from typing import List, Dict, Optional, Tuple
from src.graph.vertex import Vertex
import sys
from src.priority_queue.priority_queue import PriorityQueue


INFINITY = sys.maxsize


def heuristic(vertex: Vertex, end_vertex: Vertex):
    return vertex.position.manhattan_distance(end_vertex.position)


class Graph:
    def __init__(self):
        self.vertices: List[Vertex] = []

    def remove_vertex(self, vertex):
        vertex.remove_neighbours()

    def get_vertex_at(self, position):
        return next(filter(lambda v: v.position == position, self.vertices))

    def add_vertex(self, vertex: Vertex):
        self.vertices.append(vertex)

    def add_vertices(self, vertices):
        self.vertices.extend(vertices)

    def a_star(self, start_vertex: Vertex, end_vertex: Vertex, max_steps=sys.maxsize) -> Optional[Tuple[int, List[Vertex]]]:
        def h(vertex: Vertex):
            return heuristic(vertex, end_vertex)

        def reconstruct_path(dictionary) -> List[Vertex]:
            path = []
            current: Vertex = end_vertex
            while current != start_vertex:
                path.append(current)
                current = dictionary[current]
            path.append(current)
            return list(reversed(path))

        if start_vertex == end_vertex:
            if len(start_vertex.neighbours) > 0:
                return 2, [start_vertex, next(iter(start_vertex.neighbours)), end_vertex]
            else:
                return None

        if start_vertex.position.manhattan_distance(end_vertex.position) > max_steps:
            return None
        # TODO only return if cost is smaller than max steps

        open_set: PriorityQueue = PriorityQueue()
        open_set.put(start_vertex, 0)
        cost_dict: Dict[Vertex, int] = {vertex: INFINITY for vertex in self.vertices}
        cost_dict[start_vertex] = 0
        came_from: Dict[Vertex, Vertex] = {}
        while not open_set.empty():
            most_promising_vertex = open_set.get()
            if most_promising_vertex == end_vertex:
                return cost_dict[end_vertex], reconstruct_path(came_from)

            for neighbour in most_promising_vertex.neighbours:
                new_cost = cost_dict[most_promising_vertex] + most_promising_vertex.distance(neighbour)
                if new_cost < cost_dict[neighbour]:
                    cost_dict[neighbour] = new_cost
                    came_from[neighbour] = most_promising_vertex
                    priority = new_cost + h(neighbour)
                    # the priority is the shortest path that can be achieved, so when the shortest path is greater than max-STEPS
                    # IT DOES NOT HAVE TO BE ADDED
                    if priority < max_steps:
                        open_set.put(neighbour, priority)
        return None

    def __repr__(self):
        string = ""
        for v in self.vertices:
            string += v.position.__repr__()
            string += " -> "
            for neighbour in v.neighbours:
                string += neighbour.__repr__()
            string += "\n"
        return string
