"""
		Кузнецов Антон Денисович 
		ИВТ 1.1, 2 курс
"""
from random import *


def main():
    guess = randint(0, 100)
    x = None
    more = 'загадонное число больше'
    less = 'загадонное число меньше'
    print('Отгадайте число: ')
    while x != guess:
        x = int(input())
        if x < guess:
            print('Неверный ответ, {}'.format(more))
        elif x > guess:
            print('Неверный ответ, {}'.format(less))
        else:
            print('В точку!')



main()