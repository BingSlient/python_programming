"""Practice: return a function in a function
"""

def createCounter():
    """Create a counter increasing counts when caling it
    
    Returns:
        function: a counter increasing counts by one
    """
    global i  # use global variable
    i = 0

    def counter():
        global i
        i += 1
        return  i
    
    return counter


if __name__ == "__main__":
    counterA = createCounter()
    print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
    counterB = createCounter()
    if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
        print('测试通过!')
    else:
        print('测试失败!')