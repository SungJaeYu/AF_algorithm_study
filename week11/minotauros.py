import sys

WALL = '#'
BLANK = '.'
MESSAGE = "Impossible"


def input_data():
    w, h = map(int, sys.stdin.readline().split())
    maze = []
    for _ in range(h):
        row = list(sys.stdin.readline())
        maze.append(row)

    return w, h, maze

def convert_
