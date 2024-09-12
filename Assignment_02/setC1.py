import math

def minkowski_distance(p1, p2, p):
    return sum(abs(x - y) ** p for x, y in zip(p1, p2)) ** (1 / p)

# Example usage
point1 = (1, 2, 3)
point2 = (4, 5, 6)
p = 3  # Change this value to compute different Minkowski distances

distance = minkowski_distance(point1, point2, p)
print(f"Minkowski Distance: {distance:.4f}")