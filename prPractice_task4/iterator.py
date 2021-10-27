import random


class Iterator:

    def __init__(self, length, start, end):
        self.length = length
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        while self.length > 0:
            self.length -= 1
            return random.randint(self.start, self.end)
        return
