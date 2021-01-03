class Creature:
    def __init__(self):
        self.name = None
        self.type = None
        self.level = 0
        self.skills = []
        self.spells = []
        self.inventory = []
        self.HP = 10  # Health Points
        self.MP = 10  # Magic/Mana Points
        self.SP = 10  # Stamina Points
        self.XP = 0   # Experience Points

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

