import random

die1 = random.randint(1, 6)
die2 = random.randrange(6) + 1
total = die1 + die2

print('Випало ',die1,"і ",die2,"в сумі",total)