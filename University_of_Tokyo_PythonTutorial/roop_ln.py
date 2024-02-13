def construct_list(int_size):
    ln = [i for i in range(int_size)]
    return ln
print(construct_list(10) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])