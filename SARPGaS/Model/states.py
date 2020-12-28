from experiences import Exp
import elements


class Power(Exp):
    def __init__(self):
        super().__init__()
        self.damage = elements.get_element_damage()
        self.damage["Natural_damage"] = 1


class Defense(Exp):
    def __init__(self):
        super().__init__()
        self.resistance = elements.get_element_resistance()
        self.resistance["Natural_resistance"] = 0
        self.resistance["Magic_resistance"] = 0


class Vitality(Exp):
    def __init__(self):
        super().__init__()
        self.max_hp = 1
        self.current_hp = self.max_hp
        self.regeneration = 0
        self.regeneration_rate = 0


class Magic(Exp):
    def __init__(self):
        super().__init__()
        self.max_mana = 1
        self.current_mana = self.max_mana


if __name__ == "__main__":
    pass
