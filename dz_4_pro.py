# ДЗ 4 Про
import random
from collections import Counter
from collections import deque

# 1. Напишите функцию (F): на вход список имен и целое число N;
# на выходе список длины N случайных имен из первого списка (могут повторяться,
# можно взять значения: количество имен 20, N = 100, рекомендуется использовать функцию random);
list_n = ['Коля', 'Вася', 'Петя', 'Саша', 'Лена', 'Люся', 'Антон', 'Фёкла', 'Фиоктист', 'Павлик', 'Тарас', 'Оксана',
          'Женя', 'Ольга', 'Фёкла', 'Катя', 'Марина', 'Дима', 'Наташа', 'Пётр']
N = 10


def list_name(a, b):
    return random.sample(a, b)


lst = list_name(list_n, N)
print('Список случайных имён N раз: ', lst)


# 2. Напишите функцию вывода самого частого имени из списка на выходе функции F;
def name(arg):
    return max(set(list_n), key=arg.count)


n = name(lst)
print('Самое частое имя в списке -', n)


# 3. Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции
def counter(a):
    name = Counter(a)
    print(name)
    n = min(name)
    print('Самое редкое имя', n)
    latter = n[0]
    return print('Самая редкая буква, с которой начинаются имена в списке:', latter)


counter(list_n)


# В файле с логами найти дату самого позднего лога (по метке времени)
with open('log.py') as f:
    last_line = deque(f, maxlen=1).pop()

print('Дата последнего лога:', last_line)