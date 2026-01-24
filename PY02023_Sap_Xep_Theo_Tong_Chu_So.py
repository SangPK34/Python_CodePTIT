def tong(n):
    s = str(n)
    A = 0
    for x in s:
        A += int(x)
    return A

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ds = []
    for x in a:
        ds.append((x, tong(x)))
    ds.sort(key=lambda x: (x[1], x[0]))
    for x in ds:
        print(x[0], end=' ')
    print()
