import sys
from decimal import Decimal, ROUND_FLOOR


def doi_diem(x):
    if x >= 39:
        return Decimal('9.0')
    if x >= 37:
        return Decimal('8.5')
    if x >= 35:
        return Decimal('8.0')
    if x >= 33:
        return Decimal('7.5')
    if x >= 30:
        return Decimal('7.0')
    if x >= 27:
        return Decimal('6.5')
    if x >= 23:
        return Decimal('6.0')
    if x >= 20:
        return Decimal('5.5')
    if x >= 16:
        return Decimal('5.0')
    if x >= 13:
        return Decimal('4.5')
    if x >= 10:
        return Decimal('4.0')
    if x >= 7:
        return Decimal('3.5')
    if x >= 5:
        return Decimal('3.0')
    if x >= 3:
        return Decimal('2.5')
    return Decimal('0.0')


def lam_tron_ielts(x):
    y = ((x + Decimal('0.25')) * 2).to_integral_value(rounding=ROUND_FLOOR) / 2
    return y


def giai():
    dong = sys.stdin.read().strip().splitlines()
    if not dong:
        return
    t = int(dong[0].strip())
    out = []
    for i in range(1, t + 1):
        r, l, s, w = dong[i].split()
        dr = doi_diem(int(r))
        dl = doi_diem(int(l))
        ds = Decimal(s)
        dw = Decimal(w)
        tb = (dr + dl + ds + dw) / 4
        kq = lam_tron_ielts(tb)
        out.append(f'{kq:.1f}')
    sys.stdout.write('\n'.join(out))


if __name__ == '__main__':
    giai()
