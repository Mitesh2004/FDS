import numpy as np

p1 = np.array([16, 25, 34])
p2 = np.array([43, 52, 61])

distance = np.linalg.norm(p1 - p2)

print(f"The Euclidean distance between {p1} and {p2} is {distance:.4f}")
