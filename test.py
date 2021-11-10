from graph_package import *
import unittest

class Test_Main(unittest.TestCase):
    @classmethod
    def setup_class(klass):
        print("\n###        Start Functions Tests         ###\n")

    def test_one(self):
        pass

    def test_number_vertex_edges_1(self):
        file_name = "input6.txt"
        my_graph = Graph()
        my_graph.get_data(file_name)
        actual = (my_graph.number_vertex,my_graph.number_edge)
        expected = (6,9)
        assert expected == actual

    def test_number_vertex_edges_2(self):
        file_name = "input50.txt"
        my_graph = Graph()
        my_graph.get_data(file_name)
        actual = (my_graph.number_vertex,my_graph.number_edge)
        expected = (50,86)
        assert expected == actual

    def test_number_vertex_edges_3(self):
        file_name = "usa.txt"
        my_graph = Graph()
        my_graph.get_data(file_name)
        actual = (my_graph.number_vertex,my_graph.number_edge)
        expected = (87575,121961)
        assert expected == actual

    def test_path_1(self):
        file_name = "input6.txt"
        my_graph = Graph()
        my_graph.get_data(file_name)
        shortest_part = Dijkstra(my_graph, 0)
        stp = shortest_part.path_to(5)
        arr = []
        for i in range(len(stp)):
            arr.append(int(stp.pop()))
        expected = [0,1,2,5,5]
        assert expected == arr

    def test_path_2(self):
        file_name = "input6.txt"
        my_graph = Graph()
        my_graph.get_data(file_name)
        shortest_part = Dijkstra(my_graph, 1)
        stp = shortest_part.path_to(5)
        arr = []
        for i in range(len(stp)):
            arr.append(int(stp.pop()))
        expected = [1,2,5,5]
        assert expected == arr

    def test_path_3(self):
        file_name = "input50.txt"
        my_graph = Graph()
        my_graph.get_data(file_name)
        shortest_part = Dijkstra(my_graph, 26)
        stp = shortest_part.path_to(30)
        arr = []
        for i in range(len(stp)):
            arr.append(int(stp.pop()))
        expected = [26,38,6,4,11,13,43,29,30,30]
        assert expected == arr

    def test_path_4(self):
        file_name = "input50.txt"
        my_graph = Graph()
        my_graph.get_data(file_name)
        shortest_part = Dijkstra(my_graph, 21)
        stp = shortest_part.path_to(39)
        arr = []
        for i in range(len(stp)):
            arr.append(int(stp.pop()))
        expected = [21,18,8,49,24,19,39,39]
        assert expected == arr

    def test_path_5(self):
        file_name = "usa.txt"
        my_graph = Graph()
        my_graph.get_data(file_name)
        shortest_part = Dijkstra(my_graph, 0)
        stp = shortest_part.path_to(46)
        arr = []
        for i in range(len(stp)):
            arr.append(int(stp.pop()))
        expected = [0,18,34,37,46,46]
        assert expected == arr

    def test_path_6(self):
        file_name = "usa.txt"
        my_graph = Graph()
        my_graph.get_data(file_name)
        shortest_part = Dijkstra(my_graph, 94)
        stp = shortest_part.path_to(206)
        arr = []
        for i in range(len(stp)):
            arr.append(int(stp.pop()))
        expected = [94,120,125,143,169,183,206,206]
        assert expected == arr

    def test_empty_path1(self):
        file_name = "input50.txt"
        my_graph = Graph()
        my_graph.get_data(file_name)
        shortest_part = Dijkstra(my_graph, 23)
        stp = shortest_part.path_to(4)
        assert stp is None

    def test_empty_path2(self):
        file_name = "usa.txt"
        my_graph = Graph()
        my_graph.get_data(file_name)
        shortest_part = Dijkstra(my_graph, 0)
        stp = shortest_part.path_to(10)
        assert stp is None

