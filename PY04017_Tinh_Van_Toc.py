def tomin(s):
    gio, phut = map(int, s.split(':'))
    return gio *60 + phut

class TS:
    def __init__(self, ten, dvi, dich):
        self.ten = ten
        self.dvi = dvi
        self.ma = ""
        for c in dvi.split():
            self.ma+=c[0].upper()
        for c in ten.split():
            self.ma+=c[0].upper()
        self.tgian = tomin(dich)-tomin('6:00')
        self.vt = 120/(self.tgian/60)
    def __str__(self):
        return self.ma + " " + self.ten + " " + self.dvi +  " " + f"{self.vt:.0f} Km/h"

n = int(input())
ds = []
for i in range(n):
    ds.append(TS(input().strip(), input().strip(), input().strip()))
ds.sort(key = lambda x: x.tgian)
for ts in ds:
    print(ts)
