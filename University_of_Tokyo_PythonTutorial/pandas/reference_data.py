import numpy as np
import pandas as pd

csv_df = pd.read_csv('data.csv')
# データの条件取り出し
# dataframeの'sepal_length'列の値が7より大きく、'species'列の値が3より小さいデータを抽出
print(csv_df[(csv_df['sepal_length'] > 7.0) & (csv_df['sepal_width'] < 3.0)])

# 列の追加と削除
csv_df['mycolumn']=np.random.rand(len(csv_df.index))
print(csv_df.head(10))
del csv_df['mycolumn']
print(csv_df.head(10))
# 列を追加しつつ新しいデータフレームを作成
add_column = csv_df.assign(mycolumn=np.random.rand(len(csv_df.index)))
print(add_column.head(10))
# 列を削除しつつ新しいデータフレームを作成
delete_column = add_column.drop('mycolumn', axis=1)
print(delete_column.head(10))

# 行の追加と削除
row = pd.DataFrame([[1,1,1,1, 'setosa']], columns=csv_df.columns)
add_row = pd.concat([csv_df, row], ignore_index=True)
print(add_row[-2:])
delete_row = add_row.drop(19)
print(delete_row[-2:])

# データのソート
sorted_df = csv_df.sort_values(['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
print(sorted_df.head(10))
reverce_sorted_df = csv_df.sort_values(['sepal_length', 'sepal_width', 'petal_length', 'petal_width'], ascending=False)
print(reverce_sorted_df.head(10))

# データの統計量
print(csv_df.describe())