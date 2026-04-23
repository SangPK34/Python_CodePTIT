import sys

MOD = 1000000007


def tim(n, k):
    kq = 0
    p = 1
    while k > 0:
        if k & 1:
            kq = (kq + p) % MOD
        p = (p * n) % MOD
        k >>= 1
    return kq


def giai():
    d = list(map(int, sys.stdin.buffer.read().split()))
    if not d:
        return
    t = d[0]
    p = 1
    out = []
    for _ in range(t):
        n = d[p]
        k = d[p + 1]
        p += 2
        out.append(str(tim(n, k)))
    sys.stdout.write('\n'.join(out))


if __name__ == '__main__':
    giai()
