from graph_package.Vertex import Vertex
from graph_package.Edge import Edge
"""
    Graph class
"""


class Graph:
    def __init__(self, total_vertex=0, total_edge=0):
        self.number_vertex = total_vertex   # number of vertex in the graph
        self.number_edge = total_edge       # number of edge in the graph
        self.vertex = []                    # list of object vertex
        self.edge = []                      # list of object edge
        self.adjacent = []                  # list of edge from a vertex

    def add_vertex(self, id, x_coordinate, y_coordinate):
        temp = Vertex(id, x_coordinate, y_coordinate)
        self.vertex.append(temp)

    def add_edge(self, start_vertex, end_vertex):
        temp = Edge(self.vertex[int(start_vertex)], self.vertex[int(end_vertex)])
        self.edge.append(temp)
        self.adjacent[int(start_vertex)].append(temp)

    def get_data(self, file_name):
        try:
            with open(file_name, 'r') as file:
                line_number = 0
                for line in file:
                    # the first line of the file contain the number of vertex and edge of the graph
                    if line_number == 0:
                        total_vertex, total_edge = line.split()
                        self.number_edge = int(total_edge)
                        self.number_vertex = int(total_vertex)
                        # initialize the list of adjacent
                        for i in range(int(total_vertex)):
                            self.adjacent.append([])
                        line_number += 1

                    elif line_number < (self.number_vertex + 1):
                        # format of each line vertex name, x coordinate, y coordinate
                        vertex_id, x_coordinate, y_coordinate = line.split()
                        self.add_vertex(vertex_id, x_coordinate, y_coordinate)
                        line_number += 1

                    elif line_number == (self.number_vertex + 1):
                        line_number += 1

                    else:
                        # format of each line vertex_name 1, vertex_name 2
                        start_vertex, end_vertex = line.split()
                        self.add_edge(start_vertex, end_vertex)
                        line_number += 1

        except IOError as err:
            print(f"Fail to open the {file_name} file (%s)." % err)


# Check class section
if __name__ == "__main__":
    graph = Graph()
    graph.get_data("test_graph.txt")

    print("\n==============Vertex==============\n")
    for vertex in graph.vertex:
        print(vertex)

    print("\n===============Edge===============\n")
    for edge in graph.edge:
        print(edge)

    print("\n=============Adjacent=============\n")
    for i in range(len(graph.adjacent)):
        print("Vertex %d has edge:" % i)
        for edge in graph.adjacent[i]:
            print(edge)
        print()
