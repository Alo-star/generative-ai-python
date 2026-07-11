import numpy as np
print(np.eye(3)) #create a 3*3 matrix
arr =np.array([1,2,3,4])
print(arr.dtype)
arr.astype(float)

print(np.mean(arr))
print(arr[::-1])
print(arr[arr>1])

arr[arr>1]=30.2
print(arr)

print(np.arange(16).reshape(4,4))

newArr =np.array([[1,2,3,4],[4,5,6,7]])
print(newArr.flatten())

addArr = np.concatenate((np.array([1,2,3,4]),np.array([3,4,5,6])))
print(addArr)

print(np.count_nonzero([1,2,3,0,0,5,7]))

print(np.random.randint(1,10,(3,3)))

twoDArr = np.array([[1,2,3,4],[4,5,6,7]])
print(twoDArr.sum(axis=1))
print(twoDArr.sum(axis=0))

print(np.sort(twoDArr))
print(twoDArr.T)
print(arr*5)

print(arr ** 2)

A =np.array([[1,2,],[3,4,]])
B=np.array([[1,2,],[3,4,]])
print(A+B)
np.dot(A,B)

arr =np.array([1,np.nan,2])
np.nan_to_num(arr)