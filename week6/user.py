from monster import Monster
from item import ItemBox, Weapon, Armor, Accessories

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
            # HR Effect
            if self.effect_flag['HR']:
                self.hp = self.hp + 3
                if self.hp > self.max_hp:
                    self.hp = self.max_hp
            return is_death
        # Monster attack, User get damaged
        if boss_flag == True and self.effect_flag['HU']:
            monster_attack = 0
        else:
            monster_attack = monster.get_attack()
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
                # HR Effect
                if self.effect_flag['HR']:
                    self.hp = self.hp + 3
                    if self.hp > self.max_hp:
                        self.hp = self.max_hp
                return is_death
            self.get_damage(monster_attack)
            if self.hp <= 0:
                return True

