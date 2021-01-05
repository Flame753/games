from frame import Utility
from SARPGaS.Model.level_system import SkillPoints


class Identify(Utility, SkillPoints):
    def __init__(self):
        super().__init__()
        self.max_level = 3
        self.name = "Identify"
        self.description = "The ability to know an objects name and usage."


if __name__ == "__main__":
    a = Identify()
    print(a.at_max(), a.level, a.max_level)
