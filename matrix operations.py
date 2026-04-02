import numpy as np
matrix_a = np.array([
    [70, 75, 80],
    [60, 65, 70],
    [80, 85, 90]
])
matrix_b = np.array([
    [75, 80, 85],
    [65, 70, 75],
    [85, 90, 95]
])
addition = matrix_a + matrix_b
print(addition)
subtraction = matrix_b - matrix_a
print(subtraction)
elementwise = matrix_a * matrix_b
print(elementwise)
matrix_mult = np.dot(matrix_a, matrix_b)
print(matrix_mult)
