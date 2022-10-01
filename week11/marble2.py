import sys


UP = 1
DOWN = 2
RIGHT = 3
LEFT = 4
DIRECTIONS = [UP, DOWN, RIGHT, LEFT]

SUCCESS = 1
MOVE_DONE = 2
FAIL = 3

def input_data():
    n, m = map(int, sys.stdin.readline().split())
    input_map = []
    for _ in range(n):
        row = sys.stdin.readline()
        row = list(row)
        input_map.append(row)
    return n, m, input_map

def move_up(position):
    n, m = position
    new_position = (n-1, m)
    return new_position

def move_down(position):
    n, m = position
    new_position = (n+1, m)
    return new_position
    
def move_right(position):
    n, m = position
    new_position = (n, m+1)
    return new_position

def move_left(position):
    n, m = position
    new_position = (n, m-1)
    return new_position

def move(red, blue, hole, marble_map, direction):
    red_done = False
    blue_done = False
    hole_done = False
    move_func = {UP : move_up,
                 DOWN : move_down,
                 RIGHT : move_right,
                 LEFT : move_left}

    while red_done == False or blue_done == False:
        if not red_done:
            red_prev = red
            red_next = move_func[direction](red)
            if marble_map[red_next] != '#':
                red = red_next
            else:
                red_done = True
            if red == hole:
                red_done = True
                hole_done = True
        if not blue_done:
            blue_prev = blue
            blue_next = move_func[direction](blue)
            if marble_map[blue_next] != '#':
                blue = blue_next
            else:
                blue_done = True
            if blue == hole:
                blue_done = True
                hole_done = True

        if red == blue and hole_done == False:
            return red_prev, blue_prev
     
    return red, blue


def check_result(red, blue, hole):
    if blue == hole:
        return FAIL
    elif red == hole:
        return SUCCESS
    else:
        return MOVE_DONE

def bfs(marble_map, red, blue, hole):
    queue = []
    queue.append([red, blue, 0])
    visited = set()
    visited.add((red, blue))
    while queue:
        red, blue, move_num = queue.pop(0)
        print(f"Red : ({red[0]}, {red[1]})  Blue : ({blue[0]}, {blue[1]})")
        new_move_num = move_num + 1
        for direction in DIRECTIONS:
            red_new, blue_new = move(red, blue, hole, marble_map, direction)
            if (red_new, blue_new) not in visited:
                result = check_result(red_new, blue_new, hole)
                if result == SUCCESS:
                    return new_move_num
                elif result == MOVE_DONE:
                    visited.add((red_new, blue_new))
                    queue.append([red_new, blue_new, new_move_num])
    
    return -1
                    

def convert_map(n, m, input_map):
    marble_map = dict()
    for i in range(0, n):
        for j in range(0, m):
            if input_map[i][j] == 'R':
                marble_map[(i, j)] = '.'
                red_marble = (i, j)
            elif input_map[i][j] == 'B':
                marble_map[(i, j)] = '.'
                blue_marble = (i, j)
            elif input_map[i][j] == 'O':
                marble_map[(i, j)] = '.'
                hole = (i, j)
            else:
                marble_map[(i, j)] = input_map[i][j]
    
    return marble_map, red_marble, blue_marble, hole
            
def main():
    n, m, input_map = input_data()
    marble_map, red, blue, hole = convert_map(n, m, input_map)
    result = bfs(marble_map, red, blue, hole)
    print(result)


main()
