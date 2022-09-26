import sys


def dfs(v, graph, visited):
    visited[v] = True
    print(v)
    for vertex in graph[v]:
        if not visited[vertex]:
            dfs(vertex, graph, visited)


def maze_search():
    n, m = map(int, sys.stdin.readline().split())
    maze = []
    for _ in range(n):
        row = sys.stdin.readline().strip()
        row_list = list(row)
        maze.append(row_list)
    
    visited = dict() 
    graph = dict()
    for i in range(n):
        for j in range(m):
            if maze[i][j] == '1':
                position = (i, j)
                visited[position] = False
                graph[position] = []
                if (i-1, j) in graph:
                    graph[(i-1, j)].append(position)
                if (i, j-1) in graph:
                    graph[(i, j-1)].append(position)
                if (i+1, j) in graph:
                    graph[(i+1, j)].append(position)
                if (i, j+1) in graph:
                    graph[(i, j+1)].append(position)
    start = (0, 0)
    dfs(start, graph, visited)
     
maze_search()           

   
