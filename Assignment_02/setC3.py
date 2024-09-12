import numpy as np

# Sample arrays
array1 = np.array([0, 13])
array2 = np.array([24, 5])

# Compute the cross-correlation
cross_correlation = np.correlate(array1, array2, mode='full')

print("Original array1:")
print(array1)
print("Original array2:")
print(array2)
print("Cross-correlation of the said arrays:")
print(cross_correlation)