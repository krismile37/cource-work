Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def insert_sort(array):
    for i in range(len(array)):
        v = array[i]
        j = i
        while (array[j-1] > v) and (j > 0):
            array[j] = array[j-1]
            j = j - 1
        array[j] = v
        print array
    return array
