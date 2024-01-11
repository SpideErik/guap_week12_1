def calc_uniq(lst):
    cnt = 0
    for i in lst:
        if lst.count(i) == 1:
            cnt += 1
    return cnt


a = input('Список1>').split()
b = input('Список2>').split()

ca = calc_uniq(a)
cb = calc_uniq(b)

print(f'в списке {a} {ca} уникальных элементов')
print(f'в списке {b} {cb} уникальных элементов')
if ca > cb:
    print(f'в списке {a} больше уникальных элементов')
elif ca < cb:
    print(f'в списке {b} больше уникальных элементов')
else:
    print('В списках одинаковое число уникальных элементов')
