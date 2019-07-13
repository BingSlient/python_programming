"""Use function sorted() to sort a list by key function
"""
if __name__ == "__main__":
    L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    L1 = sorted(L, key=lambda x: x[0])
    print(L1)