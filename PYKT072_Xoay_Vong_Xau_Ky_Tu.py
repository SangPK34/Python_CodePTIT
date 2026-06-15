n = int(input())
a = []
for i in range(n):
    a.append(input().strip())
kq = 10**9
dich = a[0]
m = len(a[0])
for i in range(m):
    tong = 0
    ok = True
    for s in a:
        pos = (s + s).find(dich)
        if pos == -1 or pos >= m:
            ok = False
            break
        tong += pos
    if ok:
        kq = min(kq, tong)
    dich = dich[1:] + dich[0]
if kq == 10**9:
    print(-1)
else:
    print(kq)