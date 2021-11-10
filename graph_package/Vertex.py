"""
    Vertex class
"""


class Vertex:
    def __init__(self, id=0, x_coordinate=0, y_coordinate=0):
        # initialize all the parameter to zero if no value
        self.id = id                    # Name of the vertex, can be number or string
        self.x = int(x_coordinate)      # x and y coordinate of the vertex
        self.y = int(y_coordinate)
        self.neighbor = []              # list of connected vertex

    def coordinate(self, x_coordinate, y_coordinate):
        # update new coordinate
        self.x = int(x_coordinate)
        self.y = int(y_coordinate)

    def append_neighbor(self, neighbor):
        if neighbor not in self.neighbor:
            self.neighbor.append(neighbor)
            return True
        return False

    def delete_neighbor(self, neighbor):
        if neighbor in self.neighbor:
            self.neighbor.remove(neighbor)
            return True
        return False

    def to_string(self):
        return f"{self.id} ({self.x},{self.y})"

    def __str__(self):
        return f"{self.id}({self.x},{self.y})"


# Check class section
if __name__ == "__main__":
    a = Vertex()
    print(a.to_string())
    a.coordinate(10, 20)
    print(a.to_string())

    b = Vertex(1, 20, 30)
    print(b.to_string())

    c = Vertex(2, 30, 40)
    a.append_neighbor(b)
    a.append_neighbor(c)

    print(f"\nCheck neighbor of vertex %s" % a.id)

    for i in a.neighbor:
        print(i.to_string())
    a.delete_neighbor(c)
    print(f"\nCheck neighbor of vertex %s after delete vertex %s" % (a.id, c.id))
    for i in a.neighbor:
        print(i.to_string())
