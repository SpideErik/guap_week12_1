from random import randint


def get_answer(question):
    while True:
        s = input(question+'?>').lower()
        if s in ['да', 'нет']:
            return s == 'да'
        print('нужно отвечать да или нет')


def make_question():
    a = randint(1, 10)
    b = randint(1, 10)
    c = randint(0, 1)
    if c:
        return f'{a}+{b}={a + b}', True
    else:
        return f'{a}+{b}={a + b  -1}', False


def game(q_lst):
    while True:
        for q in q_lst:
            a = get_answer(q[0])
            if a != q[1]:
                print('Неправильно')
                a = get_answer('Хотите начать заново')
                if a:
                    break
                return
        else:
            print('Вы ответили правильно на все вопросы')
            return


q_lst = []
for _ in range(5):
    q_lst.append(make_question())
game(q_lst)
