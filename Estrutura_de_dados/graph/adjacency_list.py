class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for _ in range(self.vertices)]

    def add_edges(self, u, v, weight=None):
        # grafo direcionado (-1 pq containers python começam com 0 nao com 1)
        self.graph[u - 1].append([v, {'weight': weight}])
        # self.graph[v - 1].append([u,weight]) caso o grafo seja n direcionado

    def show_list(self):
        for index in range(self.vertices):
            print(f'{index + 1}:', end=' ')
            for _list in self.graph[index]:
                print(f'{_list} ->', end=' ')
            print('')
