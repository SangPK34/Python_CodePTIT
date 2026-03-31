t = int(input())
for _ in range(t):
    n = int(input())
    d = {}
    for _ in range(n):
        x = int(input())
        d[x] = d.get(x, 0) + 1
    print(min(d, key=lambda x: (-d[x], x)))