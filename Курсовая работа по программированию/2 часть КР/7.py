Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
N = 3
M = 5
A = np.random.randint(0, 10, (N, M))
print("Матрица:\n" + str(A))
Sum = A.sum()
print("Сумма элементов всей матрицы: " + str(Sum) + "\n")
Sum_column = A.sum(axis=1)
X = []
for i in range(0, N):
    n = Sum_column[i] / Sum
    X.append(n)
X = np.array(X)[: , np.newaxis]
A = np.hstack((A, X))
print("Новая матрица:\n" + str(A))
