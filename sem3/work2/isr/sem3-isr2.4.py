"""
		Кузнецов Антон Денисович 
		ИВТ 1.1, 2 курс
"""

from math import *

def square(d1, d2, h):
    a = sqrt((d1/2)**2 + (d2/2)**2)
    return a*a*2 + 4*a*h


def main():
    d1 = int(input('Insert first diagonal: '))
    d2 = int(input('Insert second diagonal: '))
    h = int(input('Insert height of prizm: '))
    print('Surface area:', square(d1, d2, h))


main()