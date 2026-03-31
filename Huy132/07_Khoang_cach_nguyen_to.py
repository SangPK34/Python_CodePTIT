n, x = map(int, input().split())

p = []
i = 2
while len(p) < n:
    ok = 1
    j = 2
    while j * j <= i:
        if i % j == 0:
            ok = 0
            break
        j += 1
    if ok:
        p.append(i)
    i += 1

a = [x]
for v in p:
    x += v
    a.append(x)

print(*a)