t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.insert(a.index(max(a)),m)
    b = []
    c = []
    for x in a:
        if x < 0:
            b.append(x)
        else:
            c.append(x)
    for x in b:
        print(x, end=" ")
    for x in c:
        print(x, end=" ")
    print()
