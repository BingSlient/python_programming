def triangles():
    pre_list = [1]
    yield(pre_list)
    while True:
        next_list = [1]
        i = 1
        while i < len(pre_list):
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
        if n == 5:
            break




