Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
N = 3
M = 5
A = np.random.randint(0, 100, (N, M))
print("Матрица:\n" + str(A))
Sum = A.sum()
B=np.sum(A)
M_sum = np.sum(A, axis=0)/np.sum(A)
A = np.vstack((A,M_sum))
print("Новая матрица:\n" + str(A))
