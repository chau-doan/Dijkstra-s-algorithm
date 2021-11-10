from graph_package.Vertex import Vertex
import math

"""
    Edge class
"""


def pythagorean(A: Vertex, B: Vertex):
    return math.sqrt((A.x - B.x) ** 2 + (A.y - B.y) ** 2)


class Edge:
    def __init__(self, start_vertex=Vertex(), end_vertex=Vertex()):
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex
        self.edge_distance = self.distance()

    def distance(self):
        return pythagorean(self.start_vertex, self.end_vertex)

    def start(self):
        return self.start_vertex

    def end(self, start_vertex):
        if self.start_vertex == start_vertex:
            return self.end_vertex
        return False

    def to_string(self):
        return f"({self.start_vertex.id},{self.end_vertex.id})"

    def __str__(self):
        return f"Edge from vertex {self.start_vertex.id} to vertex {self.end_vertex.id}."


# Check class section
if __name__ == "__main__":
    a = Vertex(1, 20, 30)
    b = Vertex(2, 10, 20)
    edge = Edge(a, b)

    status = "True" if edge.edge_distance == pythagorean(a, b) else "False"
    print("Distance correct? %s (Expected True)" % status)

    status = "True" if edge.start() == b else "False"
    print("Start vertex is %s correct? %s (Expected False)" % (b, status))

    status = "True" if edge.start() == a else "False"
    print("Start vertex is %s correct? %s (Expected True)" % (a, status))

    status = "True" if edge.end(a) == a else "False"
    print("End vertex is %s correct? %s (Expected False)" % (a, status))

    status = "True" if edge.end(a) == b else "False"
    print("End vertex is %s correct? %s (Expected True)" % (b, status))
