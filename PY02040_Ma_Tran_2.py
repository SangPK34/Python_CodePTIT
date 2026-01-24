n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
p = n-1
tren = duoi = 0
for i in range(n):
    for j in range(n):
        if j < p:
            tren += a[i][j]
        else:
            if j > p:
                duoi += a[i][j]
    p -=1
kq = abs(tren - duoi)
print("YES" if kq <= k else "NO")
print(kq)
