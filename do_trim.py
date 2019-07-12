def trim(s):
    """
    Trim spaces at the start or end of a string s and then return s after 
    removing beginning and trailing sapces.
    """
    if not s:    # If string s is empty, return s.
        return s
    
    mid = int(len(s) / 2)
    start = 0
    end  = 0

    # Divide s in two part to search the first appearance of not-space char
    # at the start or the end of s.
    for c in s[: mid]: # The left part of s.
        if c == ' ':
            start += 1
        else:
            break
    for c in s[mid - len(s):][:: -1]: # Get the right part and reverse it.
        if c == ' ':
            end -= 1
        else:
            break
    
    return s[start : (len(s) + end)]


if __name__ == "__main__":
    # test
    if trim('hello  ') != 'hello':
        print('1: ', len(trim('hello  ')))
        print('测试失败!')
    elif trim('  hello') != 'hello':
        print('2: ', len(trim('  hello')))
        print('测试失败!')
    elif trim('  hello  ') != 'hello':
        print('测试失败!')
    elif trim('  hello  world  ') != 'hello  world':
        print('测试失败!')
    elif trim('') != '':
        print('测试失败!')
    elif trim('    ') != '':
        print('测试失败!')
    else:
        print('测试成功!')

    
        
        