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
        else:
            #assert(0, 'Not exist Item Type')

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
 
