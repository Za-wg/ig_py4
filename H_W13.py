class Unit:
    def __init__(self, name, clan):
        self.name = name
        self.clan = clan
        self.health = 100
        self.power = 1
        self.agility = 1
        self.intellect = 1

    def therapy(self):
        if self.health < 100:
            self.health += 10


class Mage(Unit):
    def __init__(self, name, clan, air, fire, water):
        super().__init__(name, clan)
        self.air = air
        self.fire = fire
        self.water = water

    def augment(self):
        if self.intellect < 10:
            self.intellect += 1


class Archer(Unit):
    def __init__(self, name, clan, bow, crossbow):
        super().__init__(name, clan)
        self.bow = bow
        self.crossbow = crossbow

    def augment(self):
        if self.agility < 10:
            self.agility += 1


class Knight(Unit):
    def __init__(self, name, clan, sword, axe, pike):
        super().__init__(self, name)
        self.sword = sword
        self.axe = axe
        self.pike = pike

    def augment(self):
        if self.power < 10:
            self.power += 1
