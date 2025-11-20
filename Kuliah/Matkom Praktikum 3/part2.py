import numpy as np

matrix_a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Matrix A:\n", matrix_a)

matrix_b = np.array([[1, 1], [2, 2]])
matrix_c = np.array([[3, 3], [4, 4]])
result_add = matrix_b + matrix_c
print("\nMatrix Addition (B + C):\n", result_add)
hh
transpose_a = np.transpose(matrix_a)
print("\nTranspose of Matrix A:\n", transpose_a)