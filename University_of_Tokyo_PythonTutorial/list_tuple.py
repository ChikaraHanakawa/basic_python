def reverse_totuple(ln):
    return tuple(ln[::-1])
print(reverse_totuple([1, 2, 3, 4, 5]) == (5, 4, 3, 2, 1))