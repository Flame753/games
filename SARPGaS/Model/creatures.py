from SARPGaS.Model.stats import Stats, Magic
from math import floor


class Creature:
    def __init__(self):
        self.name = None
        self.type = None
        self.skills = []
        self.inventory = []
        self.stats = Stats()

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.stats.get_stat("vitality").current_hp > 0

    def get_level(self):
        return floor((self.stats.get_stat("power").level + self.stats.get_stat("defense").level + self.stats.get_stat(
            "vitality").level) / len(self.stats.stats_list))


class MagicCreature(Creature):
    def __init__(self):
        super().__init__()
        self.stats = Stats()
        self.stats.add_stat(Magic())
        self.spells = []

    def get_level(self):
        return floor((self.stats.get_stat("power").level + self.stats.get_stat("defense").level + self.stats.get_stat(
            "vitality").level + self.stats.get_stat("magic").level) / len(self.stats.stats_list))

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


class Slime(Monster, MagicCreature):
    def __init__(self):
        super().__init__()
        self.name = "slime"


class Humanoid(Creature):
    def __init__(self):
        super().__init__()
        self.type = "Humanoid"


class Elemental(MagicCreature):
    def __init__(self):
        super().__init__()
        self.type = "Elemental"


if __name__ == "__main__":
    s = Creature()
    m = MagicCreature()
    # s.stats.view_stat()
    # m.stats.view_stat()
    print(m.stats.get_stat("magic"))
    s.stats.get_stat("power").level = 10
    s.stats.get_stat("defense").level = 10
    print(s.get_level())

