t = int(input())
for _ in range(t):
    n, m, o = map(int, input().split())
    a = list(map(int, input().split()))
    b  = list(map(int, input().split()))
    c = list(map(int, input().split()))
    i = j = k = 0
    res = []
    while i < n and j < m and k < o:
        if a[i] == b[j] == c[k]:
            res.append(a[i])
            i += 1
            j += 1
            k += 1
        else:
            x = min(a[i], b[j], c[k])
            if a[i] == x:
                i += 1
            elif b[j] == x:
                j += 1
            elif c[k] == x:
                k += 1
    print(" ".join(map(str,res)) if len(res) else "NO")