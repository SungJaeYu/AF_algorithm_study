import Monster from monster

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
        is_level_up = check_level_up()
        if is_level_up:
            level_up()

    def check_level_up(self):
        if exp >= 5 * self.level:
            return True
        return False
    
    def level_up(self):
        self.max_hp = self.max_hp + 5
        self.attack = self.attack + 2
        self.defense = self.defense + 2
        
        self.hp = self.max_hp

    def equip_item(self, itembox):
        category = itembox.get_category()
        item = itembox.open_box()
        if category == 'W':
            self.equip_weapon(item)
        elif category == 'A':
            self.equip_armor(item)
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
        is_death = False
        if self.effect_flag['DX']:
            self.hp = self.hp - 1
        else:
            self.hp = self.hp - 5
        if self.hp <= 0:
            if self.effect_flag['RE']:
                self.reincarnation()
                is_death = False
            else:
                is_death = True
        return is_death

    def get_damage(self, attack):
        damage = max(1, attack - self.defense)
        self.hp = self.hp - damage

    def fight_monster(self, monster, boss_flag = False):
        is_death = False

        # HR Effect
        if self.effect_flag['HR']:
            self.hp = self.hp + 3
            if self.hp > self.max_hp:
                self.hp = self.max_hp
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
            return is_death
        # Monster attack, User get damaged
        if boss_flag == True and self.effect_flag['HU']:
            monster_attack = 0
        else:
            monster_attack = monster.get_attack()
        self.get_damage(monster_attack)
        
        # Check User Death
        if self.hp <= 0:
            if self.effect_flag['RE']:
                self.reincarnation()
                monster.reincarnation()
            else:
                is_death = True
                return is_death
            
        # Fights except first fight
        attack = self.attack
        while True:
            monster.get_damage(attack)
            if monster.get_hp() <= 0:
                return is_death
            self.get_damage(monster_attack)
            if self.hp <= 0:
                if self.effect_flag['RE']:
                    self.reincarnation()
                    monster.reincarnation()
                else:
                    is_death = True
                    return is_death

