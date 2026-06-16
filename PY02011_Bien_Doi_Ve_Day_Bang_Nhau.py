n = int(input())
a = list(map(int, input().split()))
kq = 10**18
for x in a:
    cnt = 0
    for z in a:
        cnt+= abs(z-x)
    if cnt<kq:
        kq = min(kq, cnt)
        so = x
print(kq, so)