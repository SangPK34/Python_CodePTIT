import sys

def giai():
    d = list(map(int, sys.stdin.buffer.read().split()))
    if not d:
        return
    t = d[0]
    p = 1
    kq = []
    for _ in range(t):
        n = d[p]
        p += 1
        a = d[p:p + n]
        p += n
        b = d[p:p + n]
        p += n
        a.sort()
        b.sort()
        ok = True
        for i in range(n):
            if a[i] > b[i]:
                ok = False
                break
        kq.append('YES' if ok else 'NO')
    sys.stdout.write('\n'.join(kq))

if __name__ == '__main__':
    giai()
