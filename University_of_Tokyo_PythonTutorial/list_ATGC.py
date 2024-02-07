def atgc_countlist(str_atgc):
    bases = ['A', 'T', 'G', 'C']
    list_count = [[str_atgc.count(bp), bp] for bp in bases]
    return list_count
print(sorted(atgc_countlist('AAGCCCCATGGTAA')) == sorted([[5, 'A'], [2, 'T'], [3, 'G'], [4, 'C']]))