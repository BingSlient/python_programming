def _odd_iter():
    """
    A generator to creat odds
    """
    n = 1
    while True:
        n += 2
        yield n

def _not_divisible(n):
    """
    Determine whether x can be divided by n
    """
    return lambda x: x % n > 0

def primes():
    """
    A generator to create primes 
    """
    # first rows 
    yield 2
    it = _odd_iter() # initial odd sequences
    while True:
        n = next(it) # get next item in sequence
        yield n # create prime
        # creat a new sequence by filtering all items that can be divided by n
        it = filter(_not_divisible(n), it) 

def is_palindrome(num):
    """
    Determine  whether a number is a palindrome, a palindrome is a string that 
    is identical to itself when it's reversed, like 12321, 454 etc..
    """

    numstr = str(num)
    return numstr == numstr[:: -1]

if __name__ == "__main__":
    # Test function is_palindrome
    print("Test function is_palindrome")
    output = filter(is_palindrome, range(1, 1000))
    print('1~1000:', list(output))
    if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
        print('测试成功!')
    else:
        print('测试失败!')

    # Test function primes
    print("Test function primes")
    it = primes()
    n = next(it)
    while n < 50:
        print(n)
        n = next(it)

    


