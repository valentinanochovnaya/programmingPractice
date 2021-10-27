import random


def generate_list(length, start, end):
    for i in range(length):
        yield random.randint(start, end)
