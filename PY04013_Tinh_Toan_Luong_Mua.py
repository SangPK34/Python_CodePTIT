def tomin(s):
    return int(s[0:2])*60 + int(s[3:])
ds = {}
idx = 1
n = int(input())
for _ in range(n):
    ten = input()
    bd = input()
    kt = input()
    tgian = tomin(kt) - tomin(bd)
    lm = float(input())
    if ten not in ds:
        ma = f"T{idx:02d}"
        idx += 1
        ds[ten] = [ma, tgian, lm]
    else:
        ds[ten][1] += tgian
        ds[ten][2] += lm
for ten, v in ds.items():
    ma, tgian, lm = v
    tb = lm / tgian * 60
    print(ma, ten, f"{tb:.2f}")

