def sum_lists(list1):
    total = 0
    for sublist in list1:
        total += sum(sublist)
    return total
print(sum_lists([[20, 5], [6, 16, 14, 5], [16, 8, 16, 17, 14], [1], [5, 3, 5, 7]]) == 158)