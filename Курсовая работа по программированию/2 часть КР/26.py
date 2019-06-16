Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
N = 4
M = 8
L = 3
K = 2
A = np.random.randint(0, 10, (N, M))
print("Матрица:\n" + str(A))
x = A[0:L ,0:K]
x_sum = x.mean()
print("Среднее арифметическое верхней левой части = " + str(x_sum) + "\n" + str(x))
y = A[L: ,0 :K]
y_sum = y.mean()
print("Среднее арифметическое нижней левой части = " + str(y_sum) + "\n" + str(y))
z = A[0:L ,K:]
z_sum = z.mean()
print("Среднее арифметическое верхней правой части = " + str(z_sum) + "\n" + str(z))
a = A[L: ,K:]
a_sum = a.mean()
print("Среднее арифметическое нижней правой части = " + str(a_sum) + "\n" + str(a))
