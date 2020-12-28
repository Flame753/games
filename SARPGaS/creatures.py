from states import Power, Defense, Vitality, Magic
import spells
import abilites
import items


class Creature:
    def __init__(self):
        self.name = None
        self.type = None
        self.level = self.power.level + self.defense.level + self.vitality.level
        self.skills = []
        self.inventory = []
        self.power = Power()
        self.defense = Defense()
        self.vitality = Vitality()

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.vitality.current_hp > 0


class MagicCreature(Creature):
    def __init__(self):
        super().__init__()
        self.level = self.power.level + self.defense.level + self.vitality.level + self.magic.level
        self.magic = Magic()
        self.spells = []

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
    pass
