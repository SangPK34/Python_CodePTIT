import sys


def giai():
    dong = sys.stdin.read().splitlines()
    if not dong:
        return
    n = int(dong[0].strip())
    a = dong[1:1 + n]

    i = 0
    kq = []
    while i < n:
        while i < n and not a[i].strip():
            i += 1
        if i >= n:
            break
        cd = a[i].strip()
        i += 1
        dem = 0
        while i < n and a[i].strip():
            dem += 1
            i += 1
        kq.append(f'{cd}: {dem}')

    sys.stdout.write('\n'.join(kq))


if __name__ == '__main__':
    giai()
