import sys


def xep_loai(dtb):
    if dtb >= 9:
        return "XUAT SAC"
    if dtb >= 8:
        return "GIOI"
    if dtb >= 7:
        return "KHA"
    if dtb >= 5:
        return "TB"
    return "YEU"


lines = [line.strip() for line in sys.stdin.read().replace("\ufeff", "").splitlines()]
lines = [line for line in lines if line]

n = int(lines[0])
idx = 1
ds = []

for i in range(1, n + 1):
    ma = f"HS{i:02d}"
    ten = lines[idx]
    idx += 1
    diem = list(map(float, lines[idx].split()))
    idx += 1

    tong = diem[0] * 2 + diem[1] * 2 + sum(diem[2:])
    dtb = round(tong / 12 + 1e-9, 1)
    ds.append((dtb, ma, ten, xep_loai(dtb)))

ds.sort(key=lambda x: (-x[0], x[1]))
for dtb, ma, ten, loai in ds:
    print(ma, ten, f"{dtb:.1f}", loai)

