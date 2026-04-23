import sys


def giai():
    d = list(map(int, sys.stdin.buffer.read().split()))
    if not d:
        return
    n = d[0]
    a = d[1:1 + n]

    chan = sorted([x for x in a if x % 2 == 0])
    le = sorted([x for x in a if x % 2 == 1], reverse=True)

    i = 0
    j = 0
    b = []
    for x in a:
        if x % 2 == 0:
            b.append(chan[i])
            i += 1
        else:
            b.append(le[j])
            j += 1

    sys.stdout.write(' '.join(map(str, b)))


if __name__ == '__main__':
    giai()
