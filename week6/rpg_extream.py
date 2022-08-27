BLANK = '.'
WALL = '#'
ITEM_BOX = 'B'
WEAPON = 'W'
ARMOR = 'A'
ORNAMENT = 'O'
TRAP = '^'
MONSTER = '&'
BOSS = 'M'
USER = '@'

MAX_ACCESSORIES_NUM = 4

class ItemBox:
    def __init__(self, r, c, t, s):
        self.R = r
        self.C = c
        self.T = t
        self.S = s

    def get_category(self):
        return self.T
    
    def open_itembox(self):
        if self.T == 'W':
            return Weapon(int(self.S))
        elif self.T == 'A':
            return Armor(int(self.S))
        else:
            return Accessories(self.S)

class Weapon:
    def __init__(self, attack):
        self.attack = attack

    def get_attack(self):
        return self.attack

class Armor(Item):
    def __init__(self, defense):
        self.defense = defense
    
    def get_defense(self):
        return self.defense

class Accessories(Item):
    EFFECT = ['HR', 'RE', 'CO', 'EX', 'DX', 'HU', 'CU']

    def __init__(self, effect):
        self.effect = effect
        assert(effect in EFFECT)    
    
    def get_effect(self):
        return self.S
        
class Game:
    def __init__(self):
        self.command_position = (0, 0)
        self.monsters = []
        self.monster_num = 0
        self.boss = None
        self.killed_name = None

        self.move_dict = {
            'R' : self.move_right,
            'L' : self.move_left,
            'U' : self.move_up,
            'D' : self.move_down,
        }

        self.area_dict = {
            BLANK : self.check_blank,
            WALL : self.check_wall,
            ITEMBOX : self.check_itembox,
            TRAP : self.check_trap,
            MONSTER : self.check_monster,
            BOSS : self.check_boss,
        }

    def run(self):
        self.set_game()
        self.move_user_all()
        self.print_result()

    def count_monster_and_item(self):
        monster_count = 0
        item_count = 0
        for row in self.game_map:
            for c in row:
                if c == MONSTER or c == BOSS:
                    monster_count += 1
                elif c == ITEM_BOX:
                    item_count += 1
                elif c == USER:
                    self.user = User(row, 
        return monster_count, item_count
                    

    def set_game(self):
        self.N, self.M = map(int, sys.stdin.readline().split())
        self.game_map = [[*sys.stdin.readline().strip()] for i in range(self.N)]
        self.monster_num, self.item_num = self.count_monster_and_item()
        self.moves = [*sys.stdin.readline().strip()]
        for i in range(self.monster_num):
            r, c, s, w, a, h, e = sys.stdin.readline().split()
            if self.game_map[r][c] == 'M':
                self.boss = Monster(r, c, s, w, a, h, e)
            else:
                self.monsters.append(Monster(r, c, s, w, a, h, e))
        for i in range(self.item_num):
            r, c, t, s = sys.stdin.readline().split()
            self.items.append(Item(r, c, t, s))
    
    def move_user_all(self):
        for move in moves:
            if self.end_flag == True:
                return
            move_user(move)
        print('Press any key to continue.')
        self.end_flag = True

    def move_user(self, move):
        self.move_dict[move]()
        r, c = self.command_position
        if r >= N or c >= M:
            return
        self.check_current_position()
        self.check_user_state()

    def check_current_position(self):
        r, c = self.command_position
        area = self.game_map[r][c]
        if area == WALL:
            return
        self.user_position = self.command_position
        self.area_dict[area]()

    def check_blank(self):
        return

    def check_wall(self):
        assert(0)

    def check_itembox(self):
        r, c = self.user_position
        for item in items:
            if r == item.R and c == item.C:
                self.user.equip_item(item)
                return
        assert(0)

    def check_trap(self):
        is_death = self.user.step_on_the_trap()
        if is_death:
            self.killed_name = 'SPIKE TRAP'
        
    def check_monster(self):
        r, c = self.user.get_position
        for monster in monsters:
            if self.user.position == monster.position:
                is_death = self.user.fight_monster(monster)
                if flag:
                    self.fail = True
                    self.killed_name = monster.get_name()
                    self.end_flag = True
                else:
                    self.game_map[r][c] = BLANK
                    self.monsters.remove(monster)
                return
        assert(0)

    def check_boss(self):
        r, c = self.boss.get_position()
        flag = self.user.fight_monster(self.boss)
        
        if flag:
            self.success = True
            self.game_map[r][c] = BLANK
        else:
            self.fail = True

        self.end_flag = True

    def move_right(self):
        self.command_position.first += 1
    
    def move_left(self):
        self.command_position.first -= 1

    def move_up(self):
        self.command_position.second -= 1

    def move_down(self):
        self.command_position.second += 1

        
