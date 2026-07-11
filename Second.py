import numpy as np
lst = [1, 2, 3, 4, 5]
arr = np.array(lst)
print(type(lst))
print(type(arr))

a = np.array([1, 2, 3, 4, 5])
b = np.zeros(5)
c = np.ones(5)
d = np.arange(1, 10)
e = np.linspace(1, 5, 5)
print(a, b, c, d, e)

x= np.array([1, 2, 3])
y= np.array([9, 8, 7])
z= np.array([4, 5, 6])
print(x+y+z)
print(x*y*z)
print(x[1:3])
print(x.sum())
print(x.max())
print(x.min())
print(np.sin(x))

matrix1 = np.array([[1,2],[3,4]])
matrix2 = np.array([[1,2],[3,4]])
print(matrix1+matrix2)


