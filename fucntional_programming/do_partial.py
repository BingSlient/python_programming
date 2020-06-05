"""Pratice how to use functools.partial
"""

from functools import partial

if __name__ == "__main__":

    int2 = partial(int, base=2)
    int8 = partial(int, base=8)
    max10 = partial(max, 10)

    print(int2('111101'))
    print(int8('16'))
    
    print('max10(5,6,7,8):{}'.format(max10(5,6,7,8)))