import random


def pick_lotto():
    lucky = random.sample(range(1, 46), 6)
    return lucky


# Test
print(__name__)
print('Test', pick_lotto())