import math
import sys


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)


data = sys.stdin.read().replace("\ufeff", "").split()
if data:
    t = int(float(data[0]))
    k = 1
    for _ in range(t):
        x1, y1, x2, y2 = map(float, data[k : k + 4])
        k += 4
        a = Point(x1, y1)
        b = Point(x2, y2)
        print(f"{a.distance(b):.4f}")

