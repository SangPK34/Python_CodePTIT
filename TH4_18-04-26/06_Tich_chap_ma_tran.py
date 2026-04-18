import sys


s = sys.stdin.read().replace("\ufeff", "").split()
if s:
    a = list(map(int, s))
    t = a[0]
    k = 1

    for _ in range(t):
        n, m = a[k], a[k + 1]
        k += 2

        img = []
        for _ in range(n):
            img.append(a[k : k + m])
            k += m

        ker = []
        for _ in range(3):
            ker.append(a[k : k + 3])
            k += 3

        total = 0
        for i in range(n - 2):
            for j in range(m - 2):
                v = 0
                for u in range(3):
                    r = img[i + u]
                    ku = ker[u]
                    v += r[j] * ku[0] + r[j + 1] * ku[1] + r[j + 2] * ku[2]
                total += v

        print(total)
