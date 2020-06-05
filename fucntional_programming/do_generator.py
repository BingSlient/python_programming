def triangles():
    """
    Using generator to print YangHui triangle
    """
    pre_list = [1]
    yield(pre_list) # initial row of triangle
    while True: 
        next_list = [1] # first item of a row is always 1
        i = 1
        while i < len(pre_list):
            # creat next row using previous row 
            next_list.append(pre_list[i-1]+pre_list[i]) 
            i += 1
        next_list.append(1)
        yield(next_list)

        pre_list = next_list

if __name__ == "__main__":
    n = 0
    for t in triangles():
        print(t)
        n += 1
        if n == 9:
            break




