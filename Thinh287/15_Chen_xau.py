import sys


def giai():
    dong = sys.stdin.read().splitlines()
    if len(dong) < 3:
        return
    s1 = dong[0]
    s2 = dong[1]
    p = int(dong[2].strip())
    i = p - 1
    kq = s2 + s1 if i <= 0 else s1[:i] + s2 + s1[i:]
    sys.stdout.write(kq)


if __name__ == '__main__':
    giai()
