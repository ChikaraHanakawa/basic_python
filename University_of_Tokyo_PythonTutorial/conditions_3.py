def exception3(x, y, z):
    if x == y:
        return z
    elif x == z:
        return y
    else:
        return x
print(exception3(1,2,2))
print(exception3(4,2,4))
print(exception3(9,3,9))