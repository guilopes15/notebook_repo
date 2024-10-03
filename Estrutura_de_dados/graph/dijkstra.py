class Heap:
    def __init__(self):
        self.heaplist = []
        self.size = 0


class MinHeap(Heap):
    def _heapsort(self, index):
        stop = False
        while (index // 2 > 0) and stop == False:
            if (
                self.heaplist[index - 1][0]
                < self.heaplist[(index - 1) // 2][0]
            ):
                self.heaplist[index - 1], self.heaplist[(index - 1) // 2] = (
                    self.heaplist[(index - 1) // 2],
                    self.heaplist[index - 1],
                )
            else:
                stop = True
            index //= 2

    # data é custo para chegar no vertice
    # index é o vertice da onde a aresta vem
    def insert(self, data, index):
        self.heaplist.append([data, index])
        self.size += 1
        self._heapsort(self.size)

    def pop_min(self):
        _, *self.heaplist = self.heaplist
        self.size -= 1
        return _

    def min_child(self):
        return self.heaplist[0]


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0] * self.vertices for _ in range(self.vertices)]

    def add_edges(self, u, v, weight):
        self.graph[u - 1][v - 1] = weight
        self.graph[v - 1][u - 1] = weight

    def show_matrix(self):
        for index in range(self.vertices):
            print(self.graph[index])

    def dijkstra(self, origin):
        # -1 corresponde a um custo infinito ou indeterminado
        cost_and_coming_from = [[-1, 0] for _ in range(self.vertices)]
        cost_and_coming_from[origin - 1] = [0, origin]
        heap = MinHeap()
        heap.insert(0, origin)
        while heap.size > 0:
            distance, vertice = heap.pop_min()
            for index in range(self.vertices):
                if self.graph[vertice - 1][index] != 0:
                    if (
                        cost_and_coming_from[index][0] == - 1
                        or cost_and_coming_from[index][0]
                        > distance + self.graph[vertice - 1][index]
                    ):
                        cost_and_coming_from[index] = [
                            distance + self.graph[vertice - 1][index],
                            vertice,
                        ]
                        heap.insert(
                            distance + self.graph[vertice - 1][index],
                            index + 1,
                        )

        return cost_and_coming_from


g = Graph(7)

g.add_edges(1,2,5)
g.add_edges(1,3,6)
g.add_edges(1,4,10)
g.add_edges(2,5,13)
g.add_edges(3,4,3)
g.add_edges(3,5,11)
g.add_edges(3,6,6)
g.add_edges(4,5,6)
g.add_edges(4,6,4)
g.add_edges(5,7,3)
g.add_edges(6,7,8)

g.show_matrix()

d = g.dijkstra(1)
print(d)