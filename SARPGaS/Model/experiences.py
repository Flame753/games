import math


class Exp:
    def __init__(self, max_level=10):
        self.xp = 0
        self.level = 0
        self.max_level = max_level
        self.table = {level: self.convert_to_xp(level) for level in range(self.max_level + 1)}

    @staticmethod
    def convert_to_xp(level):
        return (lambda x: (3 / 4) * (x ** 3))(level)

    @staticmethod
    def convert_to_level(xp):
        return (lambda y: ((4 / 3) * y) ** (1/3))(xp)

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
    # for num in range(0, 10):
    #     print(f"{num} : {e.convert_to_xp(num)}")
    #
    # print(e.table)
    # e.xp = 2000
    # while True:
    #     if e.level_up():
    #         print(e.level)
    #     else:
    #         print(e.level)
    #         break

    # print(e.table)
    # x = (lambda x: (x ** 3))(4)
    # print(x)
    # y = (lambda y: 1/(y ** -3))(4)
    # print(y)

    test = e.convert_to_xp(2)
    print(test)
    test = e.convert_to_level(test)
    print(test)




