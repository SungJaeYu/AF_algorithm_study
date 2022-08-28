import sys

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
            print(f'YOU HAVE BEEN KILLED BY {self.killed_name}')
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

WEAPON = 'W'
ARMOR = 'A'
ACCESSORIES = 'O'

class User:
    def __init__(self):
        self.max_hp = 20
        self.hp = 20
        self.attack = 2
        self.defense = 2
        self.exp = 0
        self.level = 1
        self.weapon = None
        self.armor = None
        self.accessories_num = 0
        self.effect_flag = {"HR" : False, "RE" : False, "CO" : False,
                            "EX" : False, "DX" : False, "HU" : False,
                            "CU" : False}
        self.equip_func = {WEAPON : self.equip_weapon,
                           ARMOR : self.equip_armor,
                           ACCESSORIES : self.equip_accessories}

    def take_monster_exp(self, monster_exp):
        if self.effect_flag['EX']:
            monster_exp = int(monster_exp * 1.2)
        self.exp += monster_exp
        is_level_up = self.check_level_up()
        if is_level_up:
            self.level_up()

        if self.effect_flag['HR']:
            self.hp = self.hp + 3
            if self.hp > self.max_hp:
                self.hp = self.max_hp


    def check_level_up(self):
        if self.exp >= 5 * self.level:
            return True
        return False
    
    def level_up(self):
        self.level += 1
        self.max_hp = self.max_hp + 5
        self.attack = self.attack + 2
        self.defense = self.defense + 2
        self.exp = 0
        self.hp = self.max_hp

    def equip_item(self, itembox):
        category = itembox.get_category()
        item = itembox.open_box()
        self.equip_func[category](item)

    def equip_weapon(self, weapon):
        if self.weapon is not None:
            self.attack = self.attack - self.weapon.get_attack()
            del self.weapon
        self.weapon = weapon
        self.attack = self.attack + weapon.get_attack()

    def equip_armor(self, armor):
        if self.armor is not None:
            self.defense = self.defense - self.armor.get_defense()
            del self.armor
        self.armor = armor
        self.defense = self.defense + armor.get_defense()

    def equip_accessories(self, new_acc):
        effect = new_acc.get_effect()

        if self.accessories_num == 4:
            return
        if self.effect_flag[effect] == True:
            return
        
        self.effect_flag[effect] = True
        self.accessories_num += 1

    def step_on_the_trap(self):
        is_death = False
        if self.effect_flag['DX']:
            self.hp = self.hp - 1
        else:
            self.hp = self.hp - 5
        if self.hp <= 0:
            is_death = True
        return is_death

    def get_damage(self, attack):
        damage = max(1, attack - self.defense)
        self.hp = self.hp - damage

    def reincarnation(self):
        self.effect_flag['RE'] = False
        self.hp = self.max_hp
        self.accessories_num -= 1

    def fight_monster(self, monster, boss_flag = False):
        is_death = False

        # HU Effect
        if boss_flag == True and self.effect_flag['HU']:
            self.hp = self.max_hp

        # First Fight
        # CO and DX Effect
        if self.effect_flag['CO'] and self.effect_flag['DX']:
            attack = self.attack * 3
        elif self.effect_flag['CO']:
            attack = self.attack * 2
        else:
            attack = self.attack

        # User attack, Monster get damagaed
        monster.get_damage(attack)

        # Check Monster Death
        if monster.get_hp() <= 0:
            self.take_monster_exp(monster.get_exp())
            return is_death
        # Monster attack, User get damaged
        monster_attack = monster.get_attack()
        if boss_flag == True and self.effect_flag['HU']:
            # 0 Damage
            pass
        else:
            self.get_damage(monster_attack)
        
        # Check User Death
        if self.hp <= 0:
           return True 
        # Fights except first fight
        attack = self.attack
        while True:
            monster.get_damage(attack)
            if monster.get_hp() <= 0:
                self.take_monster_exp(monster.get_exp())
                return is_death
            self.get_damage(monster_attack)
            if self.hp <= 0:
                return True

EFFECT = ['HR', 'RE', 'CO', 'EX', 'DX', 'HU', 'CU']

WEAPON = 'W'
ARMOR = 'A'
ACCESSORIE = 'O'


class ItemBox:
    def __init__(self, r, c, t, s):
        self.position = (r, c)
        self.type = t
        self.data = s

    def get_position(self):
        return self.position

    def get_category(self):
        return self.type
    
    def open_box(self):
        if self.type == WEAPON:
            return Weapon(int(self.data))
        elif self.type == ARMOR:
            return Armor(int(self.data))
        elif self.type == ACCESSORIE:
            return Accessories(self.data)

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
    def __init__(self, effect):
        self.effect = effect
    
    def get_effect(self):
        return self.effect
 
class Monster:
    def __init__(self, R, C, S, W, A, H, E):
        self.position = (R, C)
        self.name = S
        self.attack = W
        self.defense = A
        self.max_hp = H
        self.hp = H
        self.exp = E

    def get_position(self):
        return self.position

    def get_name(self):
        return self.name

    def get_attack(self):
        return self.attack

    def get_hp(self):
        return self.hp

    def get_exp(self):
        return self.exp

    def get_damage(self, attack):
        damage = max(1, attack - self.defense)
        self.hp = self.hp - damage

    def reincarnation(self):    
        self.hp = self.max_hp

def main():
    game = Game()
    game.run()

main()
