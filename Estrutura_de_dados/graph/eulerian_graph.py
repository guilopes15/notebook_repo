class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0] * self.vertices for _ in range(self.vertices)]

    def add_edges(self, u, v):
        # grafos nao direcinados e multiplos
        self.graph[u - 1][v - 1] += 1
        if u != v:
            self.graph[v - 1][u - 1] += 1

    def show_matrix(self):
        for line in range(self.vertices):
            print(self.graph[line])

    def contains_edges(self, u, v):
        if self.graph[u - 1][v - 1] == 0:
            print(f'Does not contain edges between {u} and {v}')
        else:
            print(f'Contain {self.graph[u-1][v-1]} edges between {u} and {v}')

    def has_eulerian(self):
        count = 0
        for i in range(self.vertices):
            degree = 0   # grau
            for j in range(self.vertices):
                if i == j:
                    degree += 2 * self.graph[i][j]
                else:
                    degree += self.graph[i][j]
            if degree % 2 != 0:
                count += 1

        match count:
            case 0:
                print("It's eulerian")
            case 2:
                print("It's semi-eulerian")
            case _:
                print("It's not eulerian nor semi-eulerian")
