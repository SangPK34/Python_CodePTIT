import sys
from bisect import bisect_right
from functools import lru_cache

nt = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
SMALL_K = 7

period = [1] * (SMALL_K + 1)
phi_blk = [1] * (SMALL_K + 1)
pref = [None] * (SMALL_K + 1)
pref[0] = [0]

for k in range(1, SMALL_K + 1):
    p = period[k - 1] * nt[k - 1]
    period[k] = p
    ok = bytearray(b'\x01') * p
    ok[0] = 0
    for pr in nt[:k]:
        ok[pr:p:pr] = b'\x00' * ((p - 1) // pr)
    ps = [0] * p
    c = 0
    for i in range(1, p):
        c += ok[i]
        ps[i] = c
    pref[k] = ps
    phi_blk[k] = c

def phi_nho(x, k):
    if x <= 0:
        return 0
    if k == 0:
        return x
    p = period[k]
    q, r = divmod(x, p)
    return q * phi_blk[k] + pref[k][r]

def giai():
    d = list(map(int, sys.stdin.buffer.read().split()))
    i = 0
    q = []
    while i < len(d):
        if d[i] == -1:
            break
        l = d[i]
        r = d[i + 1]
        n = d[i + 2]
        i += 3
        if l > r:
            l, r = r, l
        q.append((l, r, n))

    if not q:
        return

    nhom = {}
    for idx, (l, r, n) in enumerate(q):
        m = bisect_right(nt, n)
        nhom.setdefault(m, []).append((idx, l, r))

    ans = [0] * len(q)
    for m, ds in nhom.items():
        if m <= SMALL_K:
            for idx, l, r in ds:
                ans[idx] = phi_nho(r, m) - phi_nho(l - 1, m)
            continue

        prm = nt[:m]

        @lru_cache(maxsize=None)
        def phi(x, k):
            if x <= 0:
                return 0
            if k <= SMALL_K:
                return phi_nho(x, k)
            p = prm[k - 1]
            return phi(x, k - 1) - phi(x // p, k - 1)

        for idx, l, r in ds:
            ans[idx] = phi(r, m) - phi(l - 1, m)

    sys.stdout.write('\n'.join(map(str, ans)))

if __name__ == '__main__':
    giai()
