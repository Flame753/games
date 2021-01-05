from SARPGaS.Charactor.level_system import Experience


class Creature(Experience):
    def __init__(self):
        super().__init__()
        self.name = None
        self.type = None
        self.skills = []
        self.spells = []
        self.inventory = []
        self.max_HP = 10
        self.HP = self.max_HP  # Health Points
        self.max_MP = 10
        self.MP = self.max_MP  # Magic/Mana Points
        self.max_SP = 10
        self.SP = self.max_SP  # Stamina Points

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.HP > 0

    def cast_spell(self):
        pass


class Beast(Creature):
    def __init__(self):
        super().__init__()
        self.type = "Beast"


class Spider(Beast):
    def __init__(self):
        super().__init__()
        self.name = "Spider"
        self.max_HP = 5
        self.max_SP = 15


class Monster(Creature):
    def __init__(self):
        super().__init__()
        self.type = "Monster"


class Slime(Monster):
    def __init__(self):
        super().__init__()
        self.name = "slime"


class Humanoid(Creature):
    def __init__(self):
        super().__init__()
        self.type = "Humanoid"


class Elemental(Creature):
    def __init__(self):
        super().__init__()
        self.type = "Elemental"


if __name__ == "__main__":
    s = Creature()

