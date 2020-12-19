class Matrix:

    # Define infinity as the large enough value
    INF = 9223372036854775807

    def __init__(self, size):
        self.size = size
        self.matrix = [[self.INF for _ in range(size)] for _ in range(size)]
        for i in range(self.size):
            self.matrix[i][i] = 0

    def __getitem__(self, i):
        return self.matrix[i]

    # floyd warshall algorithm
    def floyd_warshall(self):
        for k in range(self.size):
            for i in range(self.size):
                for j in range(self.size):
                    if self.matrix[i][k] != self.INF and self.matrix[k][j] != self.INF:
                        self.matrix[i][j] = min(self.matrix[i][j], self.matrix[i][k] + self.matrix[k][j])
