def snt(n):
    if n <= 1: return 0
    if n == 2: return 1
    if n % 2 == 0: return 0
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0: return 0
    return 1

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        print("0" if not snt(a[i][j]) else "1", end = " ")
    print()
