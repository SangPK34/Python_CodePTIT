import sys

gt = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
a = list(map(int, sys.stdin.buffer.read().split()))
kq = []
for n in a[1:]:
    s, m = 0, n
    while m:
        s += gt[m % 10]
        m //= 10
    kq.append("Yes" if s == n else "No")
print('\n'.join(kq))