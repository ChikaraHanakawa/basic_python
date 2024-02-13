def sum_matrix(list1, list2):
    list3 = [[list1[i][j] + list2[i][j] for j in range(3)] for i in range(3)]
    return list3
print(sum_matrix([[1,2,3],[4,5,6],[7,8,9]], [[1,4,7],[2,5,8],[3,6,9]]) == [[2, 6, 10], [6, 10, 14], [10, 14, 18]])