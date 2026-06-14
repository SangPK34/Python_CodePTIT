import sys
sys.stdin = open("CATHI.in", "r")

class CT:
    def __init__(self, i, ngay, gio, phong):
        self.ma = f"C{i+1:03d}"
        self.ngay = ngay
        self.ssngay = ngay[6:]+ngay[3:5]+ ngay[:2]
        self.gio = gio
        self.phong = phong
    def __str__(self):
        return f"{self.ma} {self.ngay} {self.gio} {self.phong}"
n = int(input())
ds = []
for i in range(n):
    ds.append(CT(i, input(), input(), input()))
ds.sort(key = lambda x: (x.ssngay, x.gio, x.ma))
for ct in ds:
    print(ct)