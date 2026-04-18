import sys


def tien_nuoc(old, new):
    used = new - old
    if used <= 50:
        base, fee = used * 100, 2
    elif used <= 100:
        base, fee = 50 * 100 + (used - 50) * 150, 3
    else:
        base, fee = 50 * 100 + 50 * 150 + (used - 100) * 200, 5
    return (base * (100 + fee) + 50) // 100


lines = [x.strip() for x in sys.stdin.read().replace("\ufeff", "").splitlines() if x.strip()]
n = int(lines[0])
i = 1
ds = []

for k in range(1, n + 1):
    ma = f"KH{k:02d}"
    ten = lines[i]
    old = int(lines[i + 1])
    new = int(lines[i + 2])
    i += 3
    ds.append((tien_nuoc(old, new), ma, ten))

ds.sort(key=lambda x: (-x[0], x[1]))
for total, ma, ten in ds:
    print(ma, ten, total)

