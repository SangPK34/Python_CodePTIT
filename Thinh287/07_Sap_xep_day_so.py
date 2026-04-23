import sys


def giai():
    d = list(map(int, sys.stdin.buffer.read().split()))
    if not d:
        return
    t = d[0]
    p = 1
    out = []
    for _ in range(t):
        n = d[p]
        m = d[p + 1]
        p += 2
        a = d[p:p + n]
        p += n

        mx = max(a)
        vt = a.index(mx)
        a = a[:vt] + [m] + a[vt:]

        am = [x for x in a if x < 0]
        khac = [x for x in a if x >= 0]
        b = am + khac
        out.append(' '.join(map(str, b)))

    sys.stdout.write('\n'.join(out))


if __name__ == '__main__':
    giai()
