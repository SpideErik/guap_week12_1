def sub(a, b):
    if a == b:
        print('Числа равны')
        return None
    return max(a, b) - min(a, b)


a = int(input('a>'))
b = int(input('b>'))
print(f'sub({a},{b})={sub(a, b)}')
