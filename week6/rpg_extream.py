

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

class Item:
    def __init__(self, r, c, t, s):
        self.R = r
        self.C = c
        self.T = t
        self.S = s
    def get_category(self):
        return self.T

class Weapon(Item):
    def get_attack(self):
        return self.S

class Armor(Item):
    def get_defense(self):
        return self.S

class Accessories(Item):
    #EFFECT = ['HR', 'RE', 'CO', 'EX', 'DX', 'HU', 'CU']
    def get_effect(self):
        return self.S
        

class User:
    def __init__(self, R, C):
        self.default_position = (R, C)
        self.position = (R, C)
        self.max_hp = 20
        self.current_hp = 20
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

    def take_monster_exp(self, exp):
        self.exp += exp
        flag = check_level_up()
        if flag:
            level_up()

    def check_level_up(self):
        if exp >= 5 * self.level:
            return True
        return False
    
    def level_up(self):
        self.max_hp = self.max_hp + 5
        self.attack = self.attack + 2
        self.defense = self.defense + 2
        
        self.current_hp = self.max_hp

    def equip_item(self, item):
        category = item.get_category()
        if category == 'W':
            self.equip_weapon(Weapon(item))
        elif category == 'A':
            self.equip_armor(Armor(item))
        elif category == 'O':
            self.equip_accessories(item)
        else:
            assert(0)

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
        if self.effect_flag[new_acc] == True:
            return
        
        self.effect_flag[new_acc] = True
        self.accessories_num += 1

    def step_on_the_trap(self):
        if self.effect_flag['DX']:
            self.hp = self.hp - 1
        else:
            self.hp = self.hp - 5

    def get_damage(self, attack):
        damage = max(1, attack - self.defense)
        self.hp = self.hp - damage

    def check_death(self):
        if self.hp <= 0:
            if self.effect_flag['RE']:
                self.hp = self.max_hp
                self.R = self.default_R
                self.C = self.default_C
                self.effect_flag['RE'] = False
                return False
            else:
                return True

    def fight_monster(self, monster, boss_flag = False):
        if self.effect_flag['HR']:
            self.hp = self.hp + 3
        if self.hp > self.max_hp:
            self.hp = self.max_hp

        if self.effect_flag['CO'] and self.effect_flag['DX']:
            attack = self.attack * 3
        elif self.effect_flag['CO']:
            attack = self.attack * 2
        else:
            attack = self.attack
        monster.get_damage(attack)
        if monster.get_hp() <= 0:
            return True
        monster_attack = monster.get_attack()
        self.get_damage(monster_attack)
        if self.hp <= 0:
            death_flag = self.check_death()
            if death_flag:
                return False
            else:
                monster.set_max_hp()
            
        attack = self.attack
        while True:
            monster.get_damage(attack)
            if monster.get_hp() <= 0:
                return True
            self.get_damage(monster_attack)
            if self.hp <= 0:
                death_flag = self.check_death()
                if death_flag:
                    return False
                else:
                    monster.set_max_hp()


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

    def get_hp(self):
        return self.hp

    def get_exp(self):
        return self.exp

    def get_damage(self, attack):
        damage = max(1, attack - self.defense)
        self.hp = self.hp - damage

class Game:
 
    def __init__(self, N, M):
        self.user_position = (0, 0)
        self.command_position = (0, 0)
        self.user = User()
        self.monsters = []
        self.monster_num = 0
        self.boss = None

        self.map[M][N] = []

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
        self.user.step_on_the_trap()

    def check_monster(self):
        r, c = self.user_position
        for monster in monsters:
            if r == monster.R and c == monster.C:
                self.user.fight_monster(monster)
        assert(0)

    def check_boss(self):
        r, c = self.boss.get_position()
        self.user.fight_monster(self.boss)
        self.end_flag = True

    def move_right(self):
        self.command_position.first += 1
    
    def move_left(self):
        self.command_position.first -= 1

    def move_up(self):
        self.command_position.second -= 1

    def move_down(self):
        self.command_position.second += 1

        
