# 1.Написать любую функцию без параметров и функцию с параметрами
def no_params():
    print('Функция без параметров')


no_params()


def params(a, b):
    p = a + b
    print('Функция с параметрами, итог: ', p)


params(10, 15)


# 2.Написать любую функцию с возвращаемым значением и без него
def func(a):
    n = a + 100
    return n


print('Возврат значения: ', func(10))


def func_no_value():
    pass


print(func_no_value())


# 3.Написать любую lambda функцию
print(list(map(lambda x: x.upper(), ['У меня отличное настроение!!!'])))