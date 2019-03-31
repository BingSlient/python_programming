import math
from functools import reduce

def char2num(c):
    DIGITS = {'0': 0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
              '9':9}
    return DIGITS[c]

def str2int(s:str)->int:
    return reduce(lambda x, y: x*10+y, map(char2num, s))

def normalize(name:str)->str:
    name = name[0].capitalize() + name[1:].lower()
    return name

def product(num_list):
    # calculate the product of all nums in num_list
    return reduce(lambda x, y: x*y, num_list) 

def str2float(s:str)->float:
    point_ind = s.find('.')
    if point_ind != -1:
        s = s[:point_ind] + s[point_ind+1:]
        return float(str2int(s) / (10**((len(s)-point_ind))))
    else:
        return float(str2int(s))


    

if __name__ == "__main__":
    for x in [1, 2, 3, 4]:
        pass
    
    it = iter(range(5))
    while True:
        try:
            x = next(it)
        except StopIteration:
            break

    s = ['aDam', 'LISA', 'TiNa']
    std_s = map(normalize, s)
    print('previous names:\n{}\nnormalized names:\n{}'.format(s, list(std_s)))
    num_list = list(range(2,7))
    print('nums:{} product is: {}'.format(num_list, product(num_list)))
    print(str2float('456.123400001'))