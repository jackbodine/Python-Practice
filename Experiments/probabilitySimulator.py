import random


def roll_dice() -> int:
    return random.randint(1, 6)


total_rolls = 5000
count = 0

for i in range(total_rolls):
    rolls = [roll_dice() for x in range(3)]
    if 1 in rolls:
        count += 1

print(count/total_rolls)
