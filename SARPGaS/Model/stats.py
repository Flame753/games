from experiences import Exp
import elements


class StatFrame(Exp):
    def __init__(self):
        super().__init__()
        self.name = None

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Power(StatFrame):
    def __init__(self):
        super().__init__()
        self.name = "power"
        self.damage = elements.get_element_damage()
        self.damage["Natural_damage"] = 1


class Defense(StatFrame):
    def __init__(self):
        super().__init__()
        self.name = "defense"
        self.resistance = elements.get_element_resistance()
        self.resistance["Natural_resistance"] = 0
        self.resistance["Magic_resistance"] = 0


class Vitality(StatFrame):
    def __init__(self):
        super().__init__()
        self.name = "vitality"
        self.max_hp = 1
        self.current_hp = self.max_hp
        self.regeneration = 0
        self.regeneration_rate = 0


class Magic(StatFrame):
    def __init__(self):
        super().__init__()
        self.name = "magic"
        self.max_mana = 1
        self.current_mana = self.max_mana


class Stats:
    def __init__(self):
        self.stats = [Power(), Defense(), Vitality()]

    def add_stat(self, new_stat):
        self.stats.append(new_stat)

    def get_stat(self, stat):
        for stat_info in self.stats:
            if stat_info.name == stat:
                return stat_info

    def view_stat(self):
        for stat in self.stats:
            print(str(stat))


if __name__ == "__main__":
    st = Stats().stats
    print(st)
