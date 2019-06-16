Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
N = 3
M = 5
A = np.random.randint(0, 100, (N, M))
print("Матрица:\n" + str(A))
Average = A.mean(axis=1)
i = Average.argmax(axis=0)
max = Average.max(axis=0)
print("Наибольшее среднее значение: " + str(max))
