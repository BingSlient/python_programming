def trim(s):
    """
    Trim spaces at the start or end of a string s and then return s after 
    removing beginning and trailing sapces.
    """
    if not s:    # if string s is empty, return s
        return s
    start = 0
    end = -1
    for c in s:
        if c != ' ':
            break
        else:
            start += 1
    
    for c in s[::-1]:
        if c != ' ':
            break
        else:
            end -= 1

    if (start == len(s)) | (end == -(len(s) + 1)): # s is all spaces
        return ""
    else:
        return s[start: (len(s)+end+1)]

if __name__ == "__main__":
    # 测试:
    # print(trim('  hello'))
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

    
        
        