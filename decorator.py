"""Pratice how to use decarator
"""

import time
import functools

def metric(fn):
    """A decarator to display execution time of a function
    
    Args:
        fn (function): a function
    
    Returns:
        function: a function
    """

    @functools.wraps(fn) # use functools.wraps all attribues of fn to wrapper
    def wrapper(*args, **kw):
        start = time.time()
        r = fn(*args, **kw)
        end = time.time()
        duration = end - start
        print('{} executed in {} ms'.format(fn.__name__, duration))

        return r
    
    return wrapper

def log(params=None):
    """
    A decarator to display calling information of a function.
    Accept syntax:
    @log
    @log()
    @log('info')
    """
    def info(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kw):
            text = ''
            if isinstance(params, str):
                text = params
            print("begin call", text)
            r = fn(*args, **kw)
            print("end call")
            return r
        
        return wrapper

    if callable(params): # when using syntax: @log, return the wrapper
        return info(params)

    return info 
    

# 测试
@log
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@log("slow")
@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

if __name__ == "__main__":

    f = fast(11, 22)
    s = slow(11, 22, 33)
    if f != 33:
        print('测试失败!')
    elif s != 7986:
        print('测试失败!')