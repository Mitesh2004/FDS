import numpy as np
import matplotlib.pyplot as plt

# Sample data
nums = np.array([0.5, 0.7, 1.0, 1.2, 1.3, 2.1])
bins = np.array([0, 1, 2, 3])

# Compute the histogram
hist, bin_edges = np.histogram(nums, bins)

# Display the results
print("nums:", nums)
print("bins:", bins)
#print("Result:", (hist))
print("Histogram counts:", hist)
print("Bin edges:", bin_edges)

# Plot the histogram
plt.hist(nums, bins, edgecolor='black')
plt.xlabel('Bins')
plt.ylabel('Frequency')
plt.title('Histogram of nums against bins')
plt.show()
