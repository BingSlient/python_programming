def findMinAndMax(num_list):
    """Find min and max value of a list
    
    Args:
        num_list (list): a number list 
    
    Returns:
        tuple: (min, max)
    """
    if not num_list:
        return (None, None)
    
    min = num_list[0]
    max = num_list[0]

    for num in num_list: # Find the min and max
        if num < min:
            min = num
        if num > max:
            max = num
    
    return (min, max)

if __name__ == "__main__":
    # Test
    if findMinAndMax([]) != (None, None):
        print('测试失败!')
    elif findMinAndMax([7]) != (7, 7):
        print('测试失败!')
    elif findMinAndMax([7, 1]) != (1, 7):
        print('测试失败!')
    elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
        print('测试失败!')
    else:
        print('测试成功!')