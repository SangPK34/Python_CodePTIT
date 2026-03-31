t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for x in a:
        d[x] = d.get(x, 0) + 1
    kq = "NO"
    for x in sorted(d):
        if d[x] > n // 2:
            kq = x
            break
    print(kq)