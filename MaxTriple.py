import sys

rd = sys.stdin.buffer.readline
t = int(rd())
out = []
neg = -10**18

for _ in range(t):
    rd()
    s = rd().rstrip(b'\n')
    L = len(s)
    x = y = z = neg
    k = 8
    start = 0

    for p in range(1, k + 1):
        if p == k:
            end = L
        else:
            end = L * p // k
            while end < L and s[end] != 32:
                end += 1

        if start < end:
            a = list(map(int, s[start:end].split()))
            m = len(a)

            if m == 1:
                cands = (a[0],)
            elif m == 2:
                u = max(a)
                a.remove(u)
                cands = (u, a[0])
            else:
                u = max(a)
                a.remove(u)
                v = max(a)
                a.remove(v)
                w = max(a)
                cands = (u, v, w)

            for i in cands:
                if i >= x:
                    z = y
                    y = x
                    x = i
                elif i >= y:
                    z = y
                    y = i
                elif i > z:
                    z = i

        start = end + 1

    out.append(str(x + y + z))

sys.stdout.write('\n'.join(out))