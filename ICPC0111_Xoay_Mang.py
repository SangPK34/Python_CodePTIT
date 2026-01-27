t = int(input())
for _ in range(t) :
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = []
    for i in range(n) :
        if i < k:
            b.append(a[i])
        else: print(a[i], end = " ")
    for x in b:
        print(x, end = " ")
    print()
