from math import pow


class Equation:
    def __init__(self, min_point=(0, 0), max_point=(10, 10)):
        # X axis (Level)
        self.max_x = max_point[0]
        self.min_x = min_point[0]
        # Y axis (Points)
        self.max_y = max_point[1]
        self.min_y = min_point[1]

    def slope(self):
        return (self.max_y - self.min_y) / (self.max_x - self.min_x)

    def linear(self, x):
        # Linear (mx+b): m = Slope; x = Variable; b = Y intercept
        return self.slope * (x * self.min_y)

    def quadratic(self, x):
        # Quadratic: (a(x - h) ^ 2 + k): vertex=(h, k)
        def find_a(x, y, h, k):
            x_h = x - h
            return (y-k)/pow(x_h, 2)
        h = self.min_x
        k = self.min_y
        a = find_a(self.max_x, self.max_y, h, k)

        return a * (x - h)**2 + k


class PointSystem:
    def __init__(self):
        self.max_level = 10
        self.level = 0
        max_points = 5000  # The max number of points for the max level
        self.points = 0
        self.equation = Equation((0, 0), (self.max_level, max_points)).quadratic

    def at_max(self):
        if self.level == self.max_level:
            return True
        return False

    def check_level_up(self):
        amount_leveled_up = 0
        # try:
        for level in range(self.level, self.max_level):
            if self.points >= self.equation(level):
                amount_leveled_up += 1
            else:
                return amount_leveled_up
        return amount_leveled_up
        # except:
        #     pass

    def level_up(self):
        old_level = self.level
        self.level += self.check_level_up()
        if old_level < self.level:
            print(f"LEVEL UP TO {self.level}")
        else:
            print(f"Your at Max Level: {self.level}")


class SkillPoints(PointSystem):
    def __init__(self):
        super().__init__()


class Experience(PointSystem):
    def __init__(self):
        super().__init__()
        self.max_level = 50
        self.equation = Equation((0, 0), (.5, 100)).quadratic


if __name__ == "__main__":
    ex = Experience()
    for x in range(80+1):
        print(f"{x} need xp: {ex.equation(x)}")
        ex.level_up()
        ex.points += x*400
        print(f"xp: {ex.points}")
        print("_________________")



