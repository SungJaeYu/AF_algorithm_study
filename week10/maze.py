import sys

def input_maze_size():
    N, M = map(int, sys.stdin.readline().split())
    return N, M

class Maze():
    def __init__(self, N, M):
        self.size = (N, M)
        self.graph = dict()
        self.visited = set()
        self.destination = (N-1, M-1)
        self.start = (0, 0)

    def input_maze(self):
        N, M = self.size
        self.map = []
        for _ in range(N):
            row = sys.stdin.readline().strip()
            row_list = list(row)
            self.map.append(row_list)

    def convert_maze_to_graph(self):
        N, M = self.size
        for i in range(N):
            for j in range(M):
                if self.map[i][j] == '1':
                    position = (i, j)
                    adj = []
                    for neighbor in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                        x, y = neighbor
                        if x == -1 or y == -1 or x == N or y == M or self.map[x][y] != '1':
                            continue
                        adj.append(neighbor)        
                    self.graph[position] = adj

    def bfs(self):
        queue = []
        queue.append([self.start, 0])
        self.visited.add(self.start)
        while queue:
            position, distance = queue.pop(0)
            new_distance = distance + 1
            for vertex in self.graph[position]:
                if vertex not in self.visited:
                    if vertex == self.destination:
                        return new_distance
                    self.visited.add(vertex)
                    queue.append([vertex, new_distance])
        assert(0)

    def maze_search(self):
        distance = self.bfs()
        node_num = distance + 1
        print(node_num)


def main():
    N, M = input_maze_size()
    maze = Maze(N, M)
    maze.input_maze()
    maze.convert_maze_to_graph()
    maze.maze_search()

main()

