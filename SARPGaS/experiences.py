import math


class Exp:
    def __init__(self, max_level=10):
        self.xp = 0
        self.level = 0
        self.max_level = max_level
        self.table = {level: self.convert_to_xp(level) for level in range(self.max_level + 1)}

    @staticmethod
    def convert_to_xp(level):
        return math.ceil((lambda x: (3 / 4) * (x ** 3))(level))

    def level_up(self):
        try:
            xp = self.table.get(self.level + 1)
            if self.xp >= xp:
                self.level += 1
                return True
            return False
        except TypeError:
            # reached max level
            return False


if __name__ == "__main__":
    e = Exp()
    for num in range(0, 10):
        print(f"{num} : {e.convert_to_xp(num)}")

    print(e.table)
    e.xp = 2000
    while True:
        if e.level_up():
            print(e.level)
        else:
            print(e.level)
            break

