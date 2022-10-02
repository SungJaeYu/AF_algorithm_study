import sys

def input_maze():
    N, M = map(int, sys.stdin.readline().split())
    maze = [['0'] * (M + 2)]
    for _ in range(N):
        row = list(sys.stdin.readline())
        row.insert(0, '0')
        row.append('0')
        maze.append(row)
    maze.append(['0']* (M + 2))
    print(maze)
    return N, M, maze

class Maze():
    def __init__(self, N, M, maze_map):
        self.size = (N, M)
        self.graph = dict()
        self.visited = set()
        self.destination = (N, M)
        self.start = (1, 1)
        self.map = maze_map

    def convert_maze_to_graph(self):
        N, M = self.size
        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if self.map[i][j] == '1':
                    adj = []
                    neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                    for neighbor in neighbors:
                        x, y = neighbor
                        if self.map[x][y] == '1':
                            adj.append(neighbor)        
                    self.graph[(i, j)] = adj

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

    def maze_search(self):
        distance = self.bfs()
        node_num = distance + 1
        print(node_num)


def main():
    N, M, maze_map = input_maze()
    maze = Maze(N, M, maze_map)
    maze.convert_maze_to_graph()
    maze.maze_search()

main()

