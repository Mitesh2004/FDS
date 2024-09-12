import numpy as np

array = np.array([[0, 1], [2, 3]])
print("Original flattened array:")
print(array)

a = array.flatten()

max = np.max(a)
min = np.min(a)

print("\nMaximum value of the above flattened array:")
print(max)
print("Minimum value of the above flattened array:")
print(min)