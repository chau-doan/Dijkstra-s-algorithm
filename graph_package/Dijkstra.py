from graph_package.Graph import Graph
from graph_package.Min_heap import Min_heap
import sys
"""
    Dijkstra shortest path class
"""

class Dijkstra:
    def __init__(self, graph=Graph(), current_location=0):
        if current_location > graph.number_vertex:
            print("Invalid location. Initialize to 0.")
            current_location = 0
        self.start = current_location
        self.size = graph.number_vertex
        self.edge_to_vertex = [None] * graph.number_vertex                          # show the edge to vertex

        self.distance = [sys.maxsize] * graph.number_vertex                         # set all distance to infinity
        self.distance[current_location] = 0                                         # set the distance of the start location to 0

        self.p_queue = Min_heap(graph.number_vertex)                                # create priority queue
        self.p_queue.insert(current_location, 0.0)                                  # insert the start location with 0 priority

        while not self.p_queue.is_empty():                                          # relaxing all the edge in queue
            self.relax(graph, self.p_queue.get_min())

    def relax(self, graph, vertex):
        for edge in graph.adjacent[vertex]:
            temp_id = int(edge.end_vertex.id)                                            # get the id of the neighbor vertex of the edge

            # check if the distance from vertex to it's neighbor smaller than the data in distance list
            if self.distance[temp_id] > self.distance[vertex] + edge.edge_distance:
                self.distance[temp_id] = self.distance[vertex] + edge.edge_distance
                self.edge_to_vertex[temp_id] = edge
                if self.p_queue.contains(temp_id):
                    self.p_queue.change(temp_id, self.distance[temp_id])            # update the priority of the neighbor vertex
                else:
                    self.p_queue.insert(temp_id, self.distance[temp_id])            # add the neighbor vextex if does not exist in the queue


    def distance_to(self, destination):
        if 0 <= destination <= self.size:
            return self.distance[destination]
        return -1

    # check whether the path exist or not
    def path_exist(self, destination):
        if destination >= self.size:                                                # check whether the destination in the map or not
            print(f"Invalid destination.")
            return False
        if 0 <= self.distance[destination] < sys.maxsize:                          # if the exist the distance which no infinity there exist the path
            return True
        return False

    def path_to(self, destination):
        if 0 <= destination <= self.size:                                           # check whether the destination in the map or not
            path = [destination]

            if self.path_exist(destination):                                        # check if the path exist or not
                temp_edge = self.edge_to_vertex[destination]
                while temp_edge is not None:
                    path.append(temp_edge.end_vertex.id)
                    temp_edge = self.edge_to_vertex[int(temp_edge.start_vertex.id)]
                path.append(self.start)
                return path                                                         # the path will be read from tail to head
            else:
                return None
        else:
            print(f"Invalid destination.")
            return None

    def show_path_to(self, destination):
        if 0 <= destination <= self.size:
            path = self.path_to(destination)
            if path:
                display = f"{path.pop()}"
                for element in path:
                    display += f" -> {path.pop()}"
                display += f" -> {destination}"
                return display
            else:
                return "No path!"
        else:
            return f"Invalid destination."

# Check class section
if __name__ == "__main__":
    graph = Graph()
    graph.get_data("mini_map.txt")
    find = Dijkstra(graph, 30)
    print(find.show_path_to(28))
    path = find.path_to(28)
    for i in path:
        print(i)
