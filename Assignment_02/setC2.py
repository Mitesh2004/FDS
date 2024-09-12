import numpy as np

# Sample flattened array
array = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])

# Weights for each data point
weights = np.array([1, 2, 1])

# Compute the weighted average along the specified axis (axis=0 for columns)
weighted_avg = np.average(array, axis=0, weights=weights)

print("Original flattened array:")
print(array)
print("Weighted average along the specified axis:")
print(np.round(weighted_avg,1))