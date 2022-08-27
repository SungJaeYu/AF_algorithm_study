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
