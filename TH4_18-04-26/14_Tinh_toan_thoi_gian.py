import sys


def to_min(t):
    h, m = map(int, t.split(":"))
    return h * 60 + m


lines = [line.strip() for line in sys.stdin.read().replace("\ufeff", "").splitlines()]
lines = [line for line in lines if line]

n = int(lines[0])
i = 1
ds = []

for _ in range(n):
    ma = lines[i]
    ten = lines[i + 1]
    vao = to_min(lines[i + 2])
    ra = to_min(lines[i + 3])
    i += 4

    minutes = ra - vao
    ds.append((minutes, ma, ten))

ds.sort(key=lambda x: (-x[0], x[1]))
for minutes, ma, ten in ds:
    h, m = divmod(minutes, 60)
    print(ma, ten, f"{h} gio {m} phut")

