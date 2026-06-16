from datetime import datetime


class KH:
    def __init__(self, i, ten, phong, nhan, tra, dv):
        self.ma = f"KH{i+1:02d}"
        self.ten = ten
        self.phong = phong
        d1 = datetime.strptime(nhan, "%d/%m/%Y")
        d2 = datetime.strptime(tra, "%d/%m/%Y")
        self.ngay = (d2-d1).days+1
        self.dv = dv
        c = self.phong[0]
        if c == '1':
            dgia = 25
        elif c == '2':
            dgia = 34
        elif c == '3':
            dgia = 50
        elif c == '4':
            dgia = 80

        self.tien = self.ngay*dgia +dv

    def __str__(self):
        return self.ma + " " + self. ten + " " + self.phong + " " + str(self.ngay) + " " + str(self.tien)
n = int(input())
ds = []
for i in range(n):
    ds.append(KH(i, input().strip(), input().strip(), input().strip(), input().strip(), int(input().strip())))
ds.sort(key = lambda x: -x.tien)
for kh in ds:
    print(kh)