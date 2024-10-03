class Graph:
    def __init__(
        self, vertices
    ):   # vertices define o numero de linhas e colunas na matriz
        self.vertices = vertices
        self.graph = [[0] * self.vertices for _ in range(self.vertices)]

    # u e v sao vertices onde quero adcionar arestas
    def add_edges(self, u, v, weight=1):
        # substitui = for += se for grafo multiplo
        # -1 porque containers python começam com 0 nao com 1
        self.graph[u - 1][v - 1] = weight
        # self.graph[v-1][u-1] = 1 (cado o grafo nao seja direcionado)

    def show_matrix(self):
        for index in range(self.vertices):
            print(self.graph[index])
