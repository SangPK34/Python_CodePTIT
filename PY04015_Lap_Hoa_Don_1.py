class KH:
    def __init__(self, i, ten, cu, moi):
        self.ma = f"KH{i+1:02d}"
        self.ten = ten
        so = moi-cu
        self.tien = 0
        if so <=50:
            self.tien = so * 100
            pp = 0.02
        elif so <=100:
            self.tien = 50 * 100+ (so-50)*150
            pp = 0.03
        else:
            self.tien = 50 * 100 + 50 * 150 + (so-100)*200
            pp = 0.05
        self.tien = (self.tien *(1+pp) *100+50)//100
    def __str__(self):
        return self.ma + " " + self.ten + " " + str(int(self.tien))

n = int(input())
ds = []
for i in range(n):
    ten = input()
    cu = int(input())
    moi = int(input())
    ds.append(KH(i, ten, cu, moi))
ds.sort(key = lambda x: (-x.tien))
for kh in ds:
    print(kh)