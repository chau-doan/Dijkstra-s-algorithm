
"""
    min heap priority queue class optimize for graph
"""
class Min_heap:
    def __init__(self, size):
        self.p_queue = []               # priority queue
        self.size = size                # maximum size of the priority queue
        self.in_queue = [False] * size  # check whether the key in queue or not

    def contains(self, key):
        # check if the key is in the queue or not
        if key < self.size:
            return self.in_queue[key]               # complexity O(1), space consume
        else:
            print("Vertex not exist.")
            return False

    def insert(self, key, priority):
        if key > self.size:
            return False
        if not self.in_queue[key]:
            self.p_queue.append([key, priority])
            self.in_queue[key] = True
            self.heap_sort()                        # complexity O(logN)


    def get_min(self):
        # get the min key and pop it out of the queue
        if not self.is_empty():
            to_return = self.p_queue[0][0]
            self.in_queue[to_return] = False
            self.p_queue.pop(0)
            self.heap_sort()
            return to_return

    def change(self, key, priority):
        if self.in_queue[key]:
            for element in self.p_queue:
                if element[0] == key:
                    element[1] = priority
                    break
            self.heap_sort()
        else:
            return False

    def is_empty(self):
        return len(self.p_queue) == 0

    def sink(self, n, k):
        # find the largest between root and its child
        largest = k         # parent assume the largest
        left = 2 * k + 1    # left child
        right = 2 * k + 2   # right child

        # find the true largest
        if right < n and self.p_queue[largest][1] < self.p_queue[right][1]:
            largest = right

        if left < n and self.p_queue[largest][1] < self.p_queue[left][1]:
            largest = left

        if largest != k:
            self.p_queue[k], self.p_queue[largest] = self.p_queue[largest], self.p_queue[k]
            self.sink(n, largest)

    def heap_sort(self):
        # construct heap
        n = len(self.p_queue)

        # arrange the list
        for i in range(n // 2, -1, -1):
            self.sink(n, i)

        for i in range(n-1, 0, -1):
            self.p_queue[i], self.p_queue[0] = self.p_queue[0], self.p_queue[i]
            self.sink(i, 0)

        return self.p_queue

    def __str__(self):
        return str(self.p_queue)


# Check class section
if __name__ == "__main__":
    temp = Min_heap(10)
    temp.insert(0, 20)
    temp.insert(1, 10)
    temp.insert(2, 1)
    temp.insert(3, 12)
    temp.insert(4, 11)
    temp.insert(5, 13)
    temp.insert(6, 19)
    temp.insert(7, 21)
    temp.insert(8, 5)
    temp.insert(9, 9)
    print(temp)
    if not temp.is_empty():
        print("\nHeap is not empty.")
    else:
        print("Heap is empty.")

    print(f"Min is: %s\n\n" % temp.get_min())

    print(f"The queue contain [8,5]: {temp.contains(8)} (Expected True)")
    print(f"The queue contain [2,1]: {temp.contains(2)} (Expected False)\n\n")

    print("Queue after popped:")
    print(temp)

    temp.change(8, 22)
    print("\n\nQueue after changed priority of key 8:")
    print(temp)
