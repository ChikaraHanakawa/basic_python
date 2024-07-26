import pandas as pd
import numpy as np

csv_df = pd.read_csv('data.csv')
print(csv_df.head())# 引数なしなら5行表示
print(csv_df.index)
print(len(csv_df.index))

# reference dataframe
print(csv_df[:5])
print(csv_df[-5:])
print(csv_df['species'].head(5))
print(csv_df[['sepal_length', 'species']].head(5))

# iloc & loc
print(csv_df.iloc[1, 1]) # 2行目2列目
print(csv_df.iloc[1:3, 1:3]) # 2行目から3行目、2列目から3列目
print(csv_df.loc[5])