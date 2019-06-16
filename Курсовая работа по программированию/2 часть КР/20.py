Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
N = 3
M = 5
A = np.random.randint(0, 10, (N, M))
print("Матрица:\n" + str(A))
a = b = np.fliplr(A).diagonal(1)
a_prod = a.prod()
print("Элементы, которые выше побочной диагонали: \n" + str(a) + "\nСумма элементов, которые выше побочной диагонали = " + str(a_prod))
b = np.fliplr(A).diagonal(-1)
b_prod = b.prod()
print("Элементы, которые ниже побочной диагонали: \n" + str(b) + "\nСумма элементов, которые ниже побочной диагонали = " + str(b_prod))
