# from graph_package.Dijkstra import Dijkstra
# from graph_package.Graph import Graph
from graph_package import *
import time
import random
import matplotlib.pyplot as plt
import turtle
from datetime import date

"""
turtle package
pu() pen up
pd() pen down
setpos() set pen location
goto() move the pen, drawing
tracer(bool) true display drawing animation, false just show the line
hideturtle() hide the pointer of the pen
write() to display message
"""


def display_path(graph, path, pen, color="Green", size=2):
    pen.pensize(size)
    turtle.tracer(True)
    if color == "Brown":
        turtle.tracer(False)
    pen.color(color)
    for i in range(len(path) - 1, 0, -1):
        pen.pu()
        pen.setpos((graph.vertex[int(path[i])].x / 10) - 400, (graph.vertex[int(path[i])].y / 15) - 400)
        pen.pd()
        pen.goto((graph.vertex[int(path[i - 1])].x / 10) - 400, (graph.vertex[int(path[i - 1])].y / 15) - 400)
    pen.pu()


def road(graph, pen):
    turtle.tracer(False)
    pen.pensize(3)
    for edge in graph.edge:
        pen.pu()
        pen.color("Brown")
        pen.hideturtle()
        pen.setpos((edge.start_vertex.x / 10) - 400, (edge.start_vertex.y / 15) - 400)
        pen.pd()
        pen.color("Black")
        pen.write(edge.start_vertex.id,
                  font=("time new roman", 13))  # Write vertex ID, The overlapping id will be overwrite
        pen.pd()
        pen.color("Brown")
        pen.dot(12)
        pen.goto((edge.end_vertex.x / 10) - 400, (edge.end_vertex.y / 15) - 400)
        pen.dot(12)
        pen.color("Black")
        pen.write(edge.end_vertex.id, font=("time new roman", 13))

    for vertex in graph.vertex:
        pen.pu()
        pen.goto((vertex.x/10) - 400, (vertex.y/15) - 400)
        pen.pd()
        pen.dot(12)
        pen.color("Black")
        pen.write(vertex.id, font=("time new roman", 13))
    pen.pu()
    turtle.tracer(True)


def graph_visualization(graph, dijkstra_path):
    window = turtle.Screen()
    window.bgcolor("LightBlue")  # Background color (Light Blue)
    window.setup(width=1.0, height=1.0, startx=0,
                 starty=0)  # Set up window size to 100% of screen (width, height is float)
    turtle.screensize(1000, 1000)  # Set up screen size
    turtle.title("CMPE 130 DIJKSTRA group 18 (Chau Doan; Nguyen M. Duong")

    pen = turtle.Turtle()
    # Draw the graph
    road(graph, pen)

    root_x = graph.vertex[dijkstra_path.start].x
    root_y = graph.vertex[dijkstra_path.start].y
    print("Map created. Check the map!")
    destination = int(input("Enter the destination (-1 to exit): "))
    while destination != -1:
        pen.setpos((root_x / 10) - 400, (root_y / 15) - 400)
        path = None
        if destination < -1 or destination == dijkstra_path.start:
            print("Please enter correct path. The destination are current location or not exist.")
        else:
            path = dijkstra_path.path_to(destination)
            if path is None:
                print(f"No Path from {dijkstra_path.start} to {destination} exist.")
            else:
                display_path(graph, path, pen)
                print(f"Path: {dijkstra_path.show_path_to(destination)}")
        destination = int(input("Enter the destination (-1 to exit): "))
        if path is not None:
            display_path(graph, path, pen, "Brown", 3)
    window.reset()
    pen.setpos(0, 0)
    pen.color("Red")
    credit = "Credit\nChau Doan \nNguyen M. Duong \n\n\n" \
             "CMPE 130 - DIJKSTRA \nProfessor: Chao-Li Tarng\n"
    pen.write(credit, font=("Time new roman", 20), align="center")
    pen.hideturtle()
    turtle.done()


def demo():
    graph = Graph()
    graph.get_data("map.txt")
    find = Dijkstra(graph, 0)
    graph_visualization(graph, find)


def usa():
    file_name = "testing.txt"
    with open(file_name, 'w') as file:
        run = []
        x_axis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        file.write("Testing file.\n")
        time1 = time.time()
        graph = Graph()
        graph.get_data("usa.txt")
        time2 = time.time()
        file.write(f"Time loading usa.txt: ")
        file.write(str(time2 - time1))
        for i in x_axis:
            find = Dijkstra(graph, random.randint(0, 8000 * i))
            file.write(f"\n\n\n\n\nAttempt %d \n" % i)
            temp = 0
            for j in range(10):
                t1 = time.time()
                # path = find.path_to(random.randint(0, 87574))
                file.write(find.show_path_to(random.randint(0, 8000 * i)))
                t2 = time.time()
                file.write("\n")
                file.write(f"Time cost: %s \n\n" % str(t2 - t1))
                temp = temp + (t2 - t1)
            run.append(temp)
            file.write(f"Total time of attempt #%d: %s" %(i, str(temp)))
            del find
        plt.plot(x_axis, run)
        plt.title('Shortest path')
        plt.xlabel('Attempt')
        plt.ylabel('Average time')
        plt.show()


if __name__ == "__main__":
    print("CMPE 130 Project.")
    print("Chau Doan - Nguyen Minh Huy Duong")
    print(date.today())
    choice = int(input("Pick your option: \n (1) Demo mini map. \n (2) Testing USA map.\n (any) Exit.\n"))
    if choice == 1:
        demo()
    elif choice == 2:
        usa()
    print("Thank you for your time.")
