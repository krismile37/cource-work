Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
N = 3
M = 5
A = np.random.randint(0, 10, (N, M))
print("Матрица:\n" + str(A))
a = np.diagonal(A)
a_sum = a.sum()
print("Главная диагональ: \n" + str(a) + "\nСумма главной диагонали = " + str(a_sum))
b = np.fliplr(A).diagonal(0)
b_sum = b.sum()
print("Побочная диагональ: \n" + str(b) + "\nСумма побочной диагонали = " + str(b_sum))
