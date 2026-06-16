class MT:
    def __init__(self, ma, mon, hthuc):
        self.ma = ma
        self.mon = mon
        self.hthuc = hthuc
    def __str__(self):
        return self.ma + " " + self.mon + " " + self.hthuc

n = int(input())
ds = []
for i in range(n):
    ds.append(MT(input().strip(), input().strip(), input().strip()))
ds.sort(key = lambda x: x.ma)
for ct in ds:
    print(ct)