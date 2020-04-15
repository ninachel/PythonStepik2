class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.curr_value = 0

    def can_add(self, v):
        if self.curr_value + v <= self.capacity:
            return True
        else:
            return False

    def add(self, v):
        self.curr_value += v
