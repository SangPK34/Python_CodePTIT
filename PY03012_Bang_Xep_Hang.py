class SV:
    def __init__(self, ten, dung, nop):
        self.ten = " ".join(w.capitalize() for w in ten.split())
        self.dung = dung
        self.nop = nop

n = int(input())
ds = []
for _ in range(n):
    ten = input()
    dung, nop = map(int, input().split())
    ds.append(SV(ten, dung, nop))
ds.sort(key = lambda x: (-x.dung, x.nop, x.ten))
for d in ds:
    print(d.ten, d.dung, d.nop)
