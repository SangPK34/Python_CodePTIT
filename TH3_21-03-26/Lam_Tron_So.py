import sys

a = list(map(int, sys.stdin.buffer.read().split()))
kq = []
for n in a[1:]:
    m = 10
    while n >= m:
        if n % m >= m // 2:
            n += m
        n -= n % m
        m *= 10
    kq.append(str(n))
print('\n'.join(kq))