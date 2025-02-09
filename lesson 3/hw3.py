import pandas as pd
import numpy as np

# 1. Привести различные способы создания объектов типа Series
# Для создания Series можно использовать
# - списки Python или массивы NumPy
data = [1, 2, 3, 4]
s1 = pd.Series(data)
print(s1)

data_np = np.array([1, 2, 3, 4])
s2 = pd.Series(data_np)
# - скалярные значение
s3 = pd.Series(5, index=[0, 1, 2, 3])
print(s3)
# - словари
data_dict = {'a': 1, 'b': 2, 'c': 3}
s4 = pd.Series(data_dict)
print(s4)

# 2. Привести различные способы создания объектов типа DataFrame
# DataFrame. Способы создания
# - через объекты Series
s1 = pd.Series([1, 2, 3])
s2 = pd.Series([4, 5, 6])
df1 = pd.DataFrame({'col1': s1, 'col2': s2})
print(df1)
# - списки словарей
data_list = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}]
df2 = pd.DataFrame(data_list)
print(df2)
# - словари объектов Series
s1 = pd.Series([1, 2, 3])
s2 = pd.Series([4, 5, 6])
df3 = pd.DataFrame({'col1': s1, 'col2': s2})
print(df3)
# - двумерный массив NumPy
data_np = np.array([[1, 2], [3, 4]])
df4 = pd.DataFrame(data_np, columns=['col1', 'col2'])
print(df4)
# - структурированный массив Numpy
data_struct = np.array([(1, 2), (3, 4)], dtype=[
                       ('col1', 'i4'), ('col2', 'i4')])
df5 = pd.DataFrame(data_struct)
print(df5)

# 3. Объедините два объекта Series с неодинаковыми множествами ключей (индексов) так, чтобы вместо NaN было установлено значение 1
s1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s2 = pd.Series([4, 5, 6], index=['b', 'c', 'd'])

# Объединение с заменой NaN на 1
s_combined = s1.combine(s2, lambda x1, x2: x1 if not pd.isna(
    x1) else (x2 if not pd.isna(x2) else 1))
print(s_combined)

# 4. Переписать пример с транслирование для DataFrame так, чтобы вычитание происходило по СТОЛБЦАМ
rng = np.random.default_rng()
dfA = pd.DataFrame(rng.integers(0, 10, (2, 2)), columns=['a', 'b'])
column_means = dfA.mean(axis=0)

result = dfA - column_means
print(result)

# 5. На примере объектов DataFrame продемонстрируйте использование методов ffill() и bfill()

df = pd.DataFrame({
    'A': [1, None, 3, None],
    'B': [None, 5, None, 7]
})

df_filled = df.ffill()
print(df_filled)

df_filled = df.bfill()
print(df_filled)
