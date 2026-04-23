def khoa_ten(s):
    p = s.split()
    if not p:
        return ('', '', '')
    ten = p[-1].lower()
    hodem = ' '.join(p[:-1]).lower()
    return (ten, hodem, s.lower())


def giai():
    with open('SOTAY.txt', 'r', encoding='utf-8') as f:
        a = [x.strip() for x in f if x.strip()]

    ds = []
    ngay = ''
    i = 0
    while i < len(a):
        dong = a[i]
        if dong.startswith('Ngay '):
            ngay = dong[5:].strip()
            i += 1
            continue
        if i + 1 < len(a):
            ten = a[i]
            sdt = a[i + 1]
            ds.append((ten, sdt, ngay))
            i += 2
        else:
            i += 1

    ds.sort(key=lambda x: khoa_ten(x[0]))

    with open('DIENTHOAI.txt', 'w', encoding='utf-8') as f:
        for ten, sdt, ngay in ds:
            f.write(f'{ten}: {sdt} {ngay}\n')


if __name__ == '__main__':
    giai()
