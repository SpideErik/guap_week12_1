from random import randint


def create_field():
    f = []
    for _ in range(10):
        f.append([0]*10)
    return f


def print_field(f):
    for y in range(10):
        for x in range(10):
            print(f[x][y], end='')
        print()


def add_x(f):
    x = randint(0, 9)
    y = randint(0, 9)
    f[x][y] = 'X'


def calc_x(f, x, y):
    cnt = 0
    if x > 0 and y > 0 and f[x-1][y-1] == 'X':
        cnt += 1
    if y > 0 and f[x][y-1] == 'X':
        cnt += 1
    if x < 9 and y > 0 and f[x+1][y-1] == 'X':
        cnt += 1
    if x > 0 and f[x-1][y] == 'X':
        cnt += 1
    if x < 9 and f[x+1][y] == 'X':
        cnt += 1
    if x > 0 and y < 9 and f[x-1][y+1] == 'X':
        cnt += 1
    if y < 9 and f[x][y+1] == 'X':
        cnt += 1
    if x < 9 and y < 9 and f[x+1][y+1] == 'X':
        cnt += 1

    return cnt if cnt > 0 else '-'


f = create_field()
for _ in range(10):
    add_x(f)
print('Стартовая карта')
print_field(f)
for y in range(10):
    for x in range(10):
        if f[x][y] != 'X':
            f[x][y] = calc_x(f, x, y)
print('Обработанная карта')
print_field(f)
