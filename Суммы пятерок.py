class Buffer:
    def __init__(self):
        self.curr_part = []

    def add(self, *a):
        self.curr_part.extend(a)
        while len(self.curr_part) - 5 >= 0:
            print(sum(self.curr_part[0:5]))
            self.curr_part = self.curr_part[5:]

    def get_current_part(self):
        return self.curr_part
