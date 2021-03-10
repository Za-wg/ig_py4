class Unit:
    def __init__(self, name, clan):
        self.name = name
        self.clan = clan
        self.health = 100
        self._agility = 1
        self._intelligence = 1
        self._strength = 1
        self._base_skill = 1

    def therapy(self):
        if self.health < 100:
            self.health += 10

    @property
    def intelligence(self):
        return self._intelligence

    @property
    def strength(self):
        return self._strength

    @property
    def agility(self):
        return self._agility

    def __repr__(self):
        return f"strength: {self._strength}, intelligence: {self._intelligence}, agility: {self._agility}"

    def increase_base_skill(self):
        self._base_skill += 1


class Mage(Unit):
    def __init__(self, name, clan, air, fire, water):
        super().__init__(name, clan)
        self.air = air
        self.fire = fire
        self.water = water

    @property
    def intelligence(self):
        self._intelligence = self._base_skill
        return self._intelligence

    def __repr__(self):
        self._intelligence = self._base_skill
        return super().__repr__()


class Knight(Unit):
    def __init__(self, name, clan, sword, axe, pike):
        super().__init__(name, clan)
        self.sword = sword
        self.axe = axe
        self.pike = pike

    @property
    def strength(self):
        self._strength = self._base_skill
        return self._strength

    def __repr__(self):
        self._strength = self._base_skill
        return super().__repr__()


class Archer(Unit):
    def __init__(self, name, clan, bow, crossbow):
        super().__init__(name, clan)
        self.bow = bow
        self.crossbow = crossbow

    @property
    def agility(self):
        self._agility = self._base_skill
        return self._agility

    def __repr__(self):
        self._agility = self._base_skill
        return super().__repr__()


gendalf = Mage(name="Gendalf", clan=Mage, air="controls the air", fire="controls the fire", water="does't control water")
gendalf.increase_base_skill()
gendalf.increase_base_skill()
gendalf.increase_base_skill()
gendalf.increase_base_skill()
print(gendalf, 'Gendalf')

legolas = Archer(name="Legolas", clan=Archer, bow="Straight", crossbow="absent")
legolas.increase_base_skill()
legolas.increase_base_skill()
legolas.increase_base_skill()
print(legolas, "Legolas")

aragorn = Knight(name="Aragorn", clan=Knight, sword="main weapon", axe="knows how to use", pike="not the main weapon")
aragorn.increase_base_skill()
aragorn.increase_base_skill()
print(aragorn, "Aragorn")

