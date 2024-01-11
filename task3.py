from random import choice


def create_lst():
    x = ['красный', 'синий', 'зеленый', 'оранжевый', 'голубой']
    return x


lst = create_lst()
guess = choice(lst)
print('Отгадайте цвет из списка', lst)
for i in range(1, 4):
    s = input(f'Попытка {i}>')
    if s == guess:
        print('Угадали')
        break
else:
    print(f'Не угадали, было загадано {guess}')
