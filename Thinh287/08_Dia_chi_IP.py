import sys


def ktra_ip(s):
    p = s.split('.')
    if len(p) != 4:
        return False
    for x in p:
        if not x or not x.isdigit():
            return False
        if int(x) > 255:
            return False
    return True


def giai():
    dong = sys.stdin.read().splitlines()
    if not dong:
        return
    t = int(dong[0].strip())
    out = []
    for i in range(1, t + 1):
        s = dong[i].strip() if i < len(dong) else ''
        out.append('YES' if ktra_ip(s) else 'NO')
    sys.stdout.write('\n'.join(out))


if __name__ == '__main__':
    giai()
