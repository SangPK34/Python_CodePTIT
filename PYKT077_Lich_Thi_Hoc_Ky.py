from datetime import datetime


class CT:
    def __init__(self,i, mamon, ten, ngay, gio, nhom):
        self.maca = f"T{i+1:03d}"
        self.mamon = mamon
        self.ten = ten
        self.d1 = ngay
        self.d2 = gio
        self.ngay = datetime.strptime(ngay, "%d/%m/%Y")
        self.gio = datetime.strptime(gio, "%H:%M")
        self.nhom = nhom
    def __str__(self):
        return  self.maca + " " + self.mamon + " " + self.ten  + " " + self.d1 + " " + self.d2 + " " + self.nhom

n, m = map(int, input().split())
ds = []
dsmon = {}
for i in range(n):
    mamon = input()
    dsmon[mamon] = input()
for i in range(m):
    mamon, ngay, gio, nhom = input().strip().split()
    ds.append(CT(i, mamon, dsmon[mamon], ngay, gio, nhom ))
ds.sort(key = lambda x: (x.ngay, x.gio, x.mamon))
for ct in ds:
    print(ct)
