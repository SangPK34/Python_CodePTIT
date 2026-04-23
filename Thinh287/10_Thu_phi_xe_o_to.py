import sys


def giai():
    dong = sys.stdin.read().strip().splitlines()
    if not dong:
        return
    n = int(dong[0].strip())
    gia = {
        ('Xe_con', '5'): 10000,
        ('Xe_con', '7'): 15000,
        ('Xe_tai', '2'): 20000,
        ('Xe_khach', '29'): 50000,
        ('Xe_khach', '45'): 70000,
    }

    tong = {}
    thu_tu = []

    for i in range(1, n + 1):
        bs, lx, sg, huong, ngay = dong[i].split()
        if ngay not in tong:
            tong[ngay] = 0
            thu_tu.append(ngay)
        if huong == 'IN':
            tong[ngay] += gia.get((lx, sg), 0)

    out = [f'{ngay}: {tong[ngay]}' for ngay in thu_tu]
    sys.stdout.write('\n'.join(out))


if __name__ == '__main__':
    giai()
