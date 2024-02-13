def simple_match(str1, str2):
    len1, len2 = len(str1), len(str2)
    for i in range(len1 - len2 + 1):
        if str1[i:i+len2] == str2:
            return i
    return -1
print(simple_match('location', 'cat') == 2)
print(simple_match('soccer', 'cat') == -1)
print(simple_match('category', 'cat') == 0)
print(simple_match('carpet', 'cat') == -1)