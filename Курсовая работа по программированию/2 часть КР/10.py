Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
N = 5
M = 8
K = 2
A = np.random.randint(-1, 2, (N, M))
print("Матрица:\n" + str(A))
K_arr = np.array(A[:, K-1])
K_arr = K_arr[: , np.newaxis]
print("K-ый столбец: \r\n{}\n".format(K_arr))
A = A * K_arr
print("Новая матрица:\n" + str(A))
