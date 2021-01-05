class Frame:
    def __init__(self):
        super().__init__()
        self.name = None
        self.description = None

    def __str__(self):
        return self.name


class Attack(Frame):
    def __init__(self):
        super().__init__()
        self.damage = 10


class RangeAttack(Attack):
    def __init__(self):
        super().__init__()
        self.range = 20


class Defensive(Frame):
    def __init__(self):
        super().__init__()
        self.resistance = 0


class Utility(Frame):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    pass
