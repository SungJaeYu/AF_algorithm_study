

BLANK = '.'
WALL = '#'
ITEM_BOX = 'B'
WEAPON = 'W'
ARMOR = 'A'
ORNAMENT = 'O'
TRAP = '^'
MONSTER = '&'
BOSS = 'M'

MAX_ACCESSORIES_NUM = 4

class Weapon:
    def __init__(self, attack):
        self.attack = attack

    def get_attack(self):
        return self.attack

class Armor:
    def __init__(self, defense):
        self.defense = defense

    def get_defense(self):
        return self.defense

class Accessories:
    EFFECT = ['HR', 'RE', 'CO', 'EX', 'DX', 'HU', 'CU']

    def __init__(self, effect):
        self.effect = effect

    def get_effect(self):
        return self.effect
        

class User:
    def __init__(self):
        self.max_hp = 20
        self.current_hp = 20
        self.attack = 2
        self.defense = 2
        self.exp = 0
        self.level = 1
        self.weapon = None
        self.armor = None
        self.accessories_list = []
        self.accessories_num = 0
        
    def check_level_up(self):
        if exp >= 5 * self.level:
            return True
        return False
    
    def level_up(self):
        self.max_hp = self.max_hp + 5
        self.attack = self.attack + 2
        self.defense = self.defense + 2
        
        self.current_hp = self.max_hp

    def equip_weapon(self, weapon):
        if self.weapon is not None:
            self.attack = self.attack - self.weapon.get_attack()
            del self.weapon

        self.weapon = weapon
        self.attack = self.attack + weapon.get_attack()

    def equip_armor(self, armor):
        if self.armor is not None:
            self.defense = self.defense - self.armor.get_defense()
        self.armor = armor
        self.defense = self.defense + armor.get_defense()

    def equip_accessories(self, new_acc):
        if self.accessories_num == 4:
            return False
        for acc in self.accessories_list:
            if acc.get_effect() == new_acc.get_effect():
                return False
        self.accessories.append(accessories)

class Monster:
    def __init__(self, R, C, S, W, A, H, E):
        self.position = (R, C)
        self.name = S
        self.attack = W
        self.defense = A
        self.hp = H
        self.exp = E

    def get_position(self):
        return self.position

    def get_name(self):
        return self.name

    def get_attack(self):
        return self.attack

    def get_defense(self):
        return self.defense

    def get_hp(self):
        return hp

    def get_exp(self):
        return exp

class Game:
 
    def __init__(self, N, M):
        self.user_position = (0, 0)
        self.user = User()
        self.monsters = []
        self.boss = None
        self.N = N
        self.M = M

        self.map[N][M] = []

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

    def set_game(self):
        #todo

    def move_user_all(self):
        for move in moves:
            move_user(move)

    def print_result():
        area = self.map[user_position]
        self.area_dict[area]()

    def move_user(self, move):
        self.move_dict[move]()
        self.check_current_position()
        self.check_user_state()

    def check_current_position(self):
        i
    def move_right(self):
        self.user_position.first += 1
    
    def move_left(self):
        self.user_position.first -= 1

    def move_up(self):
        self.user_position.second -= 1

    def move_down(self):
        self.user_position.second += 1

        
