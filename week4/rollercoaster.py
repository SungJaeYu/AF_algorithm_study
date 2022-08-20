import sys 

class Rollercoaster():
    def __init__(self):
        self.row = 0
        self.col = 0
        self.rollercoaster_map = []
        self.move = []

    def input_rollercoaster(self):
        self.row, self.col = map(int, sys.stdin.readline().split())
        for i in range(self.row):
            row_temp = list(map(int, sys.stdin.readline().split()))
            self.rollercoaster_map.append(row_temp)
        
    '''
    Checking Functions
    '''
    def check_can_move_all_area(self):
        if self.row % 2 != 1 and self.col % 2 != 1:
            return False
        else:
            return True

    def find_min_happiness_area(self):
        min_num = 1000
        min_r = 0
        min_c = 0
        for r in range(self.row):
            for c in range(self.col):
                if r % 2 == c % 2:
                    continue
                if min_num > self.rollercoaster_map[r][c]:
                    min_num = self.rollercoaster_map[r][c]
                    min_r = r
                    min_c = c
        return min_r, min_c

    '''
    Moving Functions Start
    '''
    def set_move_right_end(self):
        for i in range(self.col - 1):
            self.move.append("R")

    def set_move_left_end(self):
        for i in range(self.col - 1):
            self.move.append("L")

    def set_move_down_end(self):
        for i in range(self.row - 1):
            self.move.append("D")

    def set_move_up_end(self):
        for i in range(self.row - 1):
            self.move.append("U")

    def set_move_down_one(self):
        self.move.append("D")

    def set_move_right_one(self):
        self.move.append("R")

    def set_move_left_one(self):
        self.move.append("L")

    def set_move_down_one(self):
        self.move.append("D")

    def set_move_up_one(self):
        self.move.append("U")
    '''
    Moving Functions End
    '''
    def move_max_happiness_all_area(self):
        if self.row % 2 == 1:
            for  i in range(self.row // 2):
                self.set_move_right_end()
                self.set_move_down_one()
                self.set_move_left_end()
                self.set_move_down_one()
            self.set_move_right_end()
        elif self.col % 2 == 1:
            for i in range(self.col // 2):
                self.set_move_down_end()
                self.set_move_right_one()
                self.set_move_up_end()
                self.set_move_right_one()
            self.set_move_down_end()
        else:
            assert(0)
   
    def move_not_min_happiness(self, min_r, min_c):
        r = 0
        c = 0
        ROW = 0
        COL = 1
        prev_area = [-1, -1]
        while True:
            if c == (self.col - 1) and r == 1:
                break
            new_r = r
            new_c = c
            if r == 0:
                if prev_area[COL] == c or min_c == c:
                    self.set_move_right_one()
                    new_c = c + 1
                else:
                    self.set_move_down_one()
                    new_r = r + 1
            else:
                if prev_area[COL] == c or min_c == c:
                    self.set_move_right_one()
                    new_c = c + 1
                else:
                    self.set_move_up_one()
                    new_r = r - 1
            prev_area[ROW] = r
            prev_area[COL] = c
            r = new_r
            c = new_c
                    
    def move_max_happiness_not_all_area(self):
        min_r, min_c = self.find_min_happiness_area()
        r = 0
        c = 0
        '''
        Move 2 Lines Every Iteration
        
        Case 1: Left Start
            Right - down - Left - down
            
            '>' Shape Move
        
        Case 2: Right Start
            Left - down - Right - (down)
            if Last check area is Final area(self.row - 1, self.col - 1),
            don't move down and End

            'C' Shape Move
        
        Case 3: 2 Line include Min Happiness area
            (down) - right - (up) - right
            But must not move to Min area
            and if Last check area is Final area(self.row - 1, self.col - 1)
            don't move down and End

            'Z' Shape Move
        '''
        while True:
            if min_r // 2 != r // 2:
                if c == 0:
                    self.set_move_right_end()
                    self.set_move_down_one()
                    self.set_move_left_end()
                    self.set_move_down_one()
                    r += 2
                else:
                    assert(c == self.col - 1)
                    self.set_move_left_end()
                    self.set_move_down_one()
                    self.set_move_right_end()
                    r += 1
                    if r == self.row - 1:
                        break
                    else:
                        self.set_move_down_one()
                        r += 1
            else:
                self.move_not_min_happiness(min_r - r, min_c)
                r += 1
                c = self.col - 1
                if r == self.row - 1:
                    break
                else:
                    self.set_move_down_one()
                    r += 1



    def move_max_happiness(self):
        can_move_all_area = self.check_can_move_all_area()
        if can_move_all_area is True:
            self.move_max_happiness_all_area()
        else:
            self.move_max_happiness_not_all_area()

    def get_move(self):
        return self.move

def main():
    rc = Rollercoaster()
    rc.input_rollercoaster()
    rc.move_max_happiness()
    moves = rc.get_move()
    for move in moves:
        print(move, end='')

main()
