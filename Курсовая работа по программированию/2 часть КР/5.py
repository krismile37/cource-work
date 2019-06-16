Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
N = 3
M = 5
A = np.random.randint(0, 100, (N, M))
print("Матрица:\n" + str(A))
Average_line = A.mean(axis=1)
Average_column = A.mean(axis=0)
Average_line = Average_line[: , np.newaxis]
A = np.hstack((A, Average_line))
Average_column = np.hstack((Average_column, [0.]))
A = np.vstack((A, Average_column))
print("Новая матрица:\n" + str(A))
