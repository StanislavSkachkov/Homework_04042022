class Clothes:
    def __init__(self, size, growth):
        self.size = size
        self.growth = growth

    def cost_size(self):
        return self.size / 6.5 + 0.5

    def cost_growth(self):
        return 2 * self.growth + 0.3

    @property
    def get_total_cost(self):
        return str(f"Общая площадь ткани {(self.size / 6.5 + 0.5 + 2 * self.growth + 0.3)}")


class Coat(Clothes):
    def __init__(self, size, growth):
        super().__init__(size, growth)
        self.total_cost_coat = round(self.size / 6.5 + 0.5)

    def __str__(self):
        return f"Общая площадь пальто {self.total_cost_coat}"


class Suit(Clothes):
    def __init__(self, size, growth):
        super().__init__(size, growth)
        self.total_cost_suit = round(2 * self.growth + 0.3)

    def __str__(self):
        return f"Общая площадь костюма {self.total_cost_suit}"


coat_1 = Coat (5, 6)
suit_1 = Suit (4, 3)
print(coat_1)
print(suit_1)
print(coat_1.get_total_cost)
print(suit_1.get_total_cost)

