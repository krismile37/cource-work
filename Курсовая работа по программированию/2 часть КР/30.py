Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
import random
N= random.randint (1,5)
M= random.randint (1,5)
A = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\n" + str(A))
row = np.sum(A, axis=0) * -1
A = np.insert(A, N, row, axis=0)
print("Новая матрица:\n" + str(A))
