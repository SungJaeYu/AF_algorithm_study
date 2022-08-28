import sys

from user import User
from monster import Monster
from item import ItemBox

BLANK = '.'
WALL = '#'
ITEM_BOX = 'B'
TRAP = '^'
MONSTER = '&'
BOSS = 'M'
USER = '@'
       
class Game:
    def __init__(self):
        self.command_position = [0, 0]
        self.turns = 0 
        self.default_position = (0, 0)
        self.user_position = (0, 0)
        self.user = User()
        self.monsters = {}
        self.monster_count = 0
        self.itemboxs = {}
        self.item_count = 0
        self.boss = None
        self.killed_name = None
        self.success = False
        self.end_flag = False

        self.move_dict = {
            'R' : self.move_right,
            'L' : self.move_left,
            'U' : self.move_up,
            'D' : self.move_down,
        }

        self.area_dict = {
            BLANK : self.check_blank,
            WALL : self.check_wall,
            ITEM_BOX : self.check_itembox,
            TRAP : self.check_trap,
            MONSTER : self.check_monster,
            BOSS : self.check_boss,
            USER : self.check_user,
        }

    def run(self):
        self.set_game()
        self.user_moves()
        self.print_result()

    def load_map(self):
        self.monster_count = 0
        self.item_count = 0
        for r, row in enumerate(self.game_map):
            for c, area in enumerate(row):
                if area == MONSTER or area == BOSS:
                    self.monster_count += 1
                elif area == ITEM_BOX:
                    self.item_count += 1
                elif area == USER:
                    self.default_position = (r, c)
                    self.user_position = (r, c) 
                    self.game_map[r][c] = BLANK 

    def print_result(self):
        if self.success or self.end_flag == False:
            r,c = self.user_position
            self.game_map[r][c] = USER
        
        for row in self.game_map:
            for c in row:
                print(c, end='')
            print()
        
        print(f'Passed Turns : {self.turns}')
        print(f'LV : {self.user.level}')
        print(f'HP : {self.user.hp}/{self.user.max_hp}')
        if self.user.weapon is not None:
            user_attack = self.user.attack - self.user.weapon.attack
            weapon_attack = self.user.weapon.attack
        else:
            user_attack = self.user.attack
            weapon_attack = 0
        print(f'ATT : {user_attack}+{weapon_attack}')
        if self.user.armor is not None:
            user_def = self.user.defense - self.user.armor.defense
            armor_def = self.user.armor.defense
        else:
            user_def = self.user.defense
            armor_def = 0
        print(f'DEF : {user_def}+{armor_def}')
        print(f'EXP : {self.user.exp}/{self.user.level * 5}')
        if self.end_flag and self.success:
            print('YOU WIN!')
        elif self.end_flag:
            print(f'YOU HAVE BEEN KILLED BY {self.killed_name}..')
        else:
            print('Press any key to continue.')       

    def set_game(self):
        self.N, self.M = map(int, sys.stdin.readline().split())
        self.game_map = [[*sys.stdin.readline().strip()] for i in range(self.N)]
        self.load_map()
        self.moves = [*sys.stdin.readline().strip()]
        for i in range(self.monster_count):
            r, c, s, w, a, h, e = sys.stdin.readline().split()
            r, c, w, a, h, e = map(int, [r, c, w, a, h , e])
            # For Start 0 Index
            r = r - 1
            c = c - 1
            if self.game_map[r][c] == 'M':
                self.boss = Monster(r, c, s, w, a, h, e)
            else:
                self.monsters[(r, c)] = Monster(r, c, s, w, a, h ,e)
        
        for i in range(self.item_count):
            r, c, t, s = sys.stdin.readline().split()
            # For Start 0 Index
            r = int(r) - 1
            c = int(c) - 1
            self.itemboxs[(r, c)] = ItemBox(r, c, t, s)
   

    def user_moves(self):
        for move in self.moves:
            if self.end_flag == True:
                return
            self.turns += 1
            self.move_user(move)

    def move_user(self, move):
        r, c = self.user_position
        self.command_position[0] = r
        self.command_position[1] = c
        self.move_dict[move]()
        self.check_current_position()

    def check_current_position(self):
        r, c = self.command_position
        if r < self.N and c < self.M and r >= 0 and c >= 0:
            area = self.game_map[r][c]
            if area != WALL:
                self.user_position = (r, c)
        r, c, = self.user_position
        area = self.game_map[r][c]
        self.area_dict[area]()
    
    def check_user(self):
        return

    def check_blank(self):
        return

    def check_wall(self):
        assert(0)

    def check_itembox(self):
        itembox = self.itemboxs.pop(self.user_position)
        r, c = self.user_position
        self.game_map[r][c] = BLANK
        self.user.equip_item(itembox)
        del itembox
        return

    def check_trap(self):
        is_death = self.user.step_on_the_trap()
        if is_death:
            if self.user.effect_flag['RE'] == True:
                self.user_position = self.default_position
                self.user.reincarnation()
                return
            self.killed_name = 'SPIKE TRAP'
            self.end_flag = True
        
    def check_monster(self):
        r, c = self.user_position
        monster = self.monsters.pop(self.user_position)
        is_death = self.user.fight_monster(monster)
        if is_death:
            if self.user.effect_flag['RE'] == True:
                self.user_position = self.default_position
                self.user.reincarnation()
                monster.reincarnation()
                return
            self.killed_name = monster.get_name()
            self.end_flag = True
        else:
            self.game_map[r][c] = BLANK
            del monster

    def check_boss(self):
        r, c = self.user_position
        is_death = self.user.fight_monster(self.boss, True)
        
        if is_death:
            if self.user.effect_flag['RE'] == True:
                self.user_position = self.default_position
                self.user.reincarnation()
                self.boss.reincarnation()
                return
            self.killed_name = self.boss.get_name()
            self.end_flag = True
        else:
            self.success = True
        
        self.end_flag = True

    def move_right(self):
        self.command_position[1] += 1
    
    def move_left(self):
        self.command_position[1] -= 1

    def move_up(self):
        self.command_position[0] -= 1

    def move_down(self):
        self.command_position[0] += 1

