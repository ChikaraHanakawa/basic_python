def reverse_lookup2(dic1):
    dic2 = {}
    for key, value in dic1.items():
        dic2[value] = key
    return dic2
print(reverse_lookup2({'apple': 3, 'pen': 5, 'orange': 7}) == {3: 'apple', 5: 'pen', 7: 'orange'})