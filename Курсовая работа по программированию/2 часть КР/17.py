Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
N = 4
M = 7
L = 2
A = np.random.randint(0, 10, (N, M))
print("Матрица:\n" + str(A))
row = np.random.randint(low=-9, high=10, size=M)
print("Строка для вставки: " + str(row))
A = np.insert(A, L, row, axis=0)
print("Новая матрица:\n" + str(A))
