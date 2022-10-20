import random


def guess_door(y_choice, a):
    car = random.randint(1, 3)
    if y_choice == car:
        if a:
            return False
        else:
            return True
    else:
        if a:
            return True
        else:
            return False
result = 0

for i in range(1000):
    choice = random.randint(1, 3)
    if guess_door(choice, True):
        result += 1

print(f'Процент победителей - {result / 10}')
