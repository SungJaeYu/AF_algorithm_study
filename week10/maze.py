from sys import stdin

def input_maze():
    N, M = map(int, stdin.readline().split())
    maze = [['0'] * (M + 2)]
    for _ in range(N):
        row = list(stdin.readline())
        row.insert(0, '0')
        row.append('0')
        maze.append(row)
    maze.append(['0']* (M + 2))
    return N, M, maze


def bfs(N, M, maze):
    start = (1, 1)
    destination = (N, M)
    visited = set()
    queue = [[start, 0]]
    visited.add(start)
    while queue:
        position, distance = queue.pop(0)
        new_distance = distance + 1
        (i, j) = position
        neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        for neighbor in neighbors:
            (n, m) = neighbor
            if neighbor not in visited and maze[n][m] == '1':
                if neighbor == destination:
                    return new_distance
                visited.add(neighbor)
                queue.append([neighbor, new_distance])


def main():
    N, M, maze = input_maze()
    result = bfs(N, M, maze)
    print(result + 1)


main()

