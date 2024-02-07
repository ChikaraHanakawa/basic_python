def exception9(a):
    for i in a:
        if a.count(i) == 1:
            return i
print(exception9([1,2,2,2,2,2,2,2,2]))
print(exception9([4,4,4,4,4,2,4,4,4]))
print(exception9([9,9,9,9,9,9,9,9,3]))