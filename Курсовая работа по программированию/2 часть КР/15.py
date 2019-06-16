Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
N = 4
M = 7
H = 3
A = np.random.randint(0, 10, (N, M))
print("Матрица:\n" + str(A))
a = []
b = []
for i in range(M):
    if H in A[:, i]:
        a.append(i+1)
    else:
        b.append(i+1)
print("Столбцы, которые имеют хотя бы одно число H: {}\n".format(a))
print("Столбцы, которые не имеют это число: {}\n".format(b))
