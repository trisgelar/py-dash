import numpy as np
import pandas as pd

df = pd.read_csv('data/salaries.csv')
print(df['Name'])

print(df[['Name','Salary']])

print(df['Salary'].min())

print(df['Salary'].mean())

# print(df['Salary'].argmin())

print(df['Salary'].idxmax())


# conditional filter
ser_of_bool = df[df['Age'] > 30]
print(ser_of_bool)

# apply

print(df['Age'].unique())
print(df['Age'].nunique())

print(df.columns)

print(df.info())

print(df.describe())

print(df.index)

# panda with numpy

# mat = np.arange(0,50).reshape(5,10)
mat = np.arange(0,10).reshape(5,2)

df_mat = pd.DataFrame(data = mat, columns=['A', 'B'])
print(df_mat)






