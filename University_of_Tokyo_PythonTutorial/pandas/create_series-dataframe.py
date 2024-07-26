import pandas as pd
import numpy as np

# リストからSeriesを作成
list_series = pd.Series([0, 1, 2])
print(list_series)
# 配列からSeriesを作成
numpy_series = pd.Series(np.random.rand(3))
print(numpy_series)
# 辞書型からSeriesを作成
dict_series = pd.Series({0:'boo', 1:'int', 2:'woo'})
print(dict_series)

# 多次元リストからDataFrameを作成
list_df = pd.DataFrame([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]], index=[10, 11, 12, 13], columns=['c1', 'c2', 'c3'])
print(list_df)
# 多次元配列からDataFrameを作成
numpy_df = pd.DataFrame(np.random.rand(12).reshape(4, 3), columns=['c1', 'c2', 'c3'])
print(numpy_df)
# 辞書型からDataFrameを作成
dict_df = pd.DataFrame({'Initial': ['B', 'F', 'W'], 'Name': ['boo', 'foo', 'woo']}, columns =['Name', 'Initial'])
print(dict_df)