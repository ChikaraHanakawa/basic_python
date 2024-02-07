def handle_collision(dic1, str1):
    n = len(str1)
    if n not in dic1:
        dic1[n] = [str1]
    else:
        dic1[n].append(str1)
    return dic1
dic1_orig = {3: ['ham', 'egg'], 6: ['coffee', 'brandy'], 9: ['port wine'], 15: ['curried chicken']}
dic1_result = {3: ['ham', 'egg', 'tea'], 6: ['coffee', 'brandy'], 9: ['port wine'], 15: ['curried chicken']}
handle_collision(dic1_orig, 'tea')
print(dic1_orig == dic1_result)