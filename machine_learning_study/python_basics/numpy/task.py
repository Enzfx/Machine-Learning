# CODE HERE
import numpy as np

arr = np.array([np.nan, 2, 3, 4, 5])
print(arr)

arr2 = arr.copy()
arr2[0] = 10
print(arr2)

float_arr = np.array([1, 5.4, 3])
print(float_arr)
float_arr2 = arr2.astype(np.float32)
print(float_arr2)

matrix = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float32)
print(matrix)