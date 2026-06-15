import math
import sys
data = sys.stdin.read().split()
t = int(data[0])
idx = 1
for _ in range(t):
    n, k = map(int, data[idx:idx+2])
    idx+=2
    a = list(map(int, data[idx:idx+n]))
    idx +=n
    kq = n + 1
    for i in range(n):
        g = 0
        for j in range(i, n):
            g = math.gcd(g, a[j])
            if g == k:
                kq = min(kq, j - i + 1)
                break
            if g % k != 0:
                break
    if kq == n + 1:
        print("-1")
    else:
        print(kq)
