import sys

rd = sys.stdin.buffer.readline
t = int(rd())
out = []
inf = 10**18

for _ in range(t):
    rd()
    s = rd().rstrip(b'\n')
    L = len(s)
    x = y = z = inf
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
            a = map(int, s[start:end].split())

            u = v = w = inf
            for i in a:
                if i <= u:
                    w = v
                    v = u
                    u = i
                elif i <= v:
                    w = v
                    v = i
                elif i < w:
                    w = i

            for i in (u, v, w):
                if i <= x:
                    z = y
                    y = x
                    x = i
                elif i <= y:
                    z = y
                    y = i
                elif i < z:
                    z = i

        start = end + 1

    out.append(str(x + y + z))

sys.stdout.write('\n'.join(out))