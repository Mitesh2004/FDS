import numpy as np
from itertools import combinations

p = np.array([[1, 2], [3, 4], [5, 6]])

sum = sum(
    np.sum(np.abs(p1 - p2)) for p1, p2 in combinations(p, 2)
)

print("The sum of Manhattan distances between all pairs of points is ::", sum)
