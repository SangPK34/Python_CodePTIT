import math
import sys
data = sys.stdin.read().split()

t = int(data[0])
idx = 1
for _ in range(t):
    x1, y1, x2, y2, x3, y3 = map(float,data[idx:idx+6])
    idx+=6
    a = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    b = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    c = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)

    if max([a,b,c]) * 2 >= a + b + c:
        print("INVALID")
        continue
    else:
        s = math.sqrt((a+b+c)*(a+b-c)*(a-b+c)*(-a+b+c)) / 4
        print(f"{s:.2f}")