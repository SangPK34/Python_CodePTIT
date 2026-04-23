import sys

data = list(map(int, sys.stdin.buffer.read().split()))
t = data[0]
idx = 1
res = []

for _ in range(t):
    n = data[idx]
    idx += 1
    a = data[idx:idx + n]
    idx += n

    ans = 0
    for i in range(n - 1):
        x, y = a[i], a[i + 1]
        if x > y:
            x, y = y, x
        while y > 2 * x:
            x *= 2
            ans += 1

    res.append(str(ans))

print('\n'.join(res))