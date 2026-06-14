import math

class P:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def kc(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

t = int(input())
for _ in range(t):
    x1, y1, x2, y2, x3, y3 = map(float, input().split())
    p1 = P(x1, y1)
    p2 = P(x2, y2)
    p3 = P(x3, y3)
    A = p1.kc(p2)
    B = p2.kc(p3)
    C = p3.kc(p1)
    if max(A, B, C) >= 1/2*(A+B+C):
        print("INVALID")
        continue
    print(f"{A+B+C:.6f}")
