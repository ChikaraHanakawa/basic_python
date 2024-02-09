def sum_n(x, y):
    total = 0
    for i in range(x, y+1):
        total += i
    return total
print(sum_n(1, 3) == 6)