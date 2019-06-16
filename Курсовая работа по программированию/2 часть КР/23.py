Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
N = 3
M = 5
A = np.random.randint(0, 10, (N, M))
print("Матрица:\n" + str(A))
iu = np.triu_indices(N, 1)
a = A[iu]
a = np.sum(np.array(a))
print("Cумма элементов выше главной диагонали = " + str(a))
b = np.fliplr(A)[iu]
b = np.prod(np.array(b))
print("Произведение элементов выше побочной диагонали = " + str(b))
