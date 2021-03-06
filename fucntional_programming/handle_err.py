"""Learn how to catch error and deal with it in python
"""

from functools import reduce
import logging

def str2num(s):
    return int(s) # change int to float to fix the problem

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    try:
        r = calc('100 + 200 + 345')
        print('100 + 200 + 345 =', r)
        r = calc('99 + 88 + 7.6')
        print('99 + 88 + 7.6 =', r)
    except Exception as e:
        logging.exception(e)

if __name__ == '__main__':
    main()
    print("END")