import sys
import math
from bisect import bisect_right


def sang(n):
    if n < 2:
        return []
    f = [True] * (n + 1)
    f[0] = f[1] = False
    r = int(n ** 0.5)
    for i in range(2, r + 1):
        if f[i]:
            b = i * i
            f[b:n + 1:i] = [False] * (((n - b) // i) + 1)
    return [i for i in range(2, n + 1) if f[i]]


def giai():
    s = sys.stdin.readline().strip()
    if not s:
        return
    n = int(s)
    s2 = int(math.isqrt(n))
    nt = sang(s2)

    kq = 0

    for p in nt:
        if p ** 8 <= n:
            kq += 1
        else:
            break

    m = len(nt)
    for i in range(m):
        lim = s2 // nt[i]
        j = bisect_right(nt, lim)
        if j > i + 1:
            kq += j - i - 1

    sys.stdout.write(str(kq))


if __name__ == '__main__':
    giai()
