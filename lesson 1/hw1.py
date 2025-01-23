import numpy as np
import array
import sys
import random

# 1. Какие еще существуют коды типов?
# 2. Напишите код, подобный приведенному выше, но с другим типом

# signed char
a1 = array.array('b', [-1, 2, -3])
print(sys.getsizeof(a1))
print(type(a1))


# unsigned char
a1 = array.array('B', [1, 2, 3])

# Unicode character 2 bytes
a1 = array.array('u', 'abc')

# Unicode character 4 bytes
# a1 = array.array('w', 'abc')

# signed short
a1 = array.array('h', [-1, 2, -3])

# unsigned short
a1 = array.array('H', [1, 2, 3])

# signed int
a1 = array.array('i', [-1, 2, -3])

# unsigned int
a1 = array.array('I', [1, 2, 3])

# signed long
a1 = array.array('l', [-1, 2, -3])

# unsigned long
a1 = array.array('L', [1, 2, 3])

# signed long long
a1 = array.array('q', [-1, 2, -3])

# unsigned long long
a1 = array.array('Q', [1, 2, 3])

# float
a1 = array.array('f', [1.0, 2.0, 3.0])

# double
a1 = array.array('d', [1.0, 2.0, 3.0])


# 3. Напишите код для создания массива с 5 значениями, располагающимися через
# равные интервалы в диапазоне от 0 до 1

print(np.linspace(0, 1, 5))

# 4. Напишите код для создания массива с 5 равномерно распределенными
# случайными значениями в диапазоне от 0 до 1

a1 = array.array('d', [random.uniform(0, 1) for _ in range(5)])
print(a1)

# 5. Напишите код для создания массива с 5 нормально распределенными
# случайными значениями с мат. ожиданием = 0 и дисперсией 1

a1 = array.array('d', [random.gauss(0, 1) for _ in range(5)])
print(a1)

# 6. Напишите код для создания массива с 5 случайными
# целыми числами в от [0, 10)

print(np.random.randint(10, size=5))
# 7. Написать код для создания срезов массива 3 на 4


a1 = np.random.randint(100, size=(3, 4))
print(a1)
# - первые две строки и три столбца
print(a1[:2, :3])
# - первые три строки и второй столбец
print(a1[:, 1:2])
# - все строки и столбцы в обратном порядке
# - второй столбец
print(a1[:, 1])
# - третья строка
print(a1[2, :])

# 8. Продемонстрируйте, как сделать срез-копию

a = np.array([1, 2, 3, 4, 5])
b = a[1:4].copy()
b[0] = 100
print(a[1])

# 9. Продемонстрируйте использование newaxis для получения вектора-столбца и
# вектора-строки

arr = np.array([1, 2, 3, 4, 5])
row_vector = arr[np.newaxis, :]
print(row_vector)
print(row_vector.shape)


col_vector = arr[:, np.newaxis]
print(col_vector)
print(col_vector.shape)

# 10. Разберитесь, как работает метод dstack

a = np.arange(5)
b = np.arange(5)
print(a, b)
print(np.dstack((a, b)))

# 11. Разберитесь, как работают методы split, vsplit, hsplit, dsplit

a = np.arange(10)
print(np.split(a, 5))

a = np.arange(16).reshape(4, 4)
print(a)
print(np.vsplit(a, 4))

print(np.hsplit(a, 2))

a = np.arange(16.0).reshape(2, 2, 4)
print(a)
# делит на соответствующее количество частей по третьему измерению
print(np.dsplit(a, 2))
# 12. Привести пример использования всех универсальных функций, которые я
# привел # np.abs, sin/cos/tan, exp, log

a = np.array([-1, -2, 12, 4, -15])

print(np.abs(a))

print(np.sin(a))

print(np.cos(a))

print(np.tan(a))

print(np.exp(a))

a = np.abs(a)

print(np.log(a))
