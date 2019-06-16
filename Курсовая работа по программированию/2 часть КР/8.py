Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
N = 5
M = 8
A = np.random.randint(-100, 100, (N, M))
print("Матрица:\n" + str(A))
Sum = A.sum()
print("Сумма элементов всей матрицы: " + str(Sum) + "\n")
X = []
for i in range(0, N):
    K = 0
    for j in range(0, M):
        if A[i,j] < 0:
            K += 1
    X.append(K)
Y = []
for i in range(0, M):
    K = 0
    for j in range(0, N):
        if A[j,i] < 0:
            K += 1
    Y.append(K)
X = np.array(X)[: , np.newaxis]
A = np.hstack((A, X))
Y = np.hstack((Y, [0.]))
A = np.vstack((A, Y))
print("Новая матрица:\n" + str(A))
