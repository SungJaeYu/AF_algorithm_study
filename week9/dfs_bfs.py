import sys
from collections import deque


def dfs(v, edges, visited):
    visited[v] = True
    print(v, end=' ')
    for vertex in edges[v]:
        if not visited[vertex]:
            dfs(vertex, edges, visited)

def bfs(v, edges, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for vertex in edges[v]:
            if not visited[vertex]:
                queue.append(vertex)
                visited[vertex] = True

def main():
    n, m, v = map(int, sys.stdin.readline().split())
    visited = [False] * (n + 1)
    edges = []
    lines = []
    for _ in range(n + 1):
        edges.append([])
    
    for _ in range(m):
        start, end = map(int, sys.stdin.readline().split())
        if start > end:
            temp = start
            start = end
            end = temp
        lines.append((start, end))
    
    lines.sort()
    
    for start, end in lines:
        edges[start].append(end)
        edges[end].append(start)
    dfs(v, edges, visited)
    print('')
    visited = [False] * (n + 1)
    bfs(v, edges, visited)

main()
