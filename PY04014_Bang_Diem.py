import math


class HS:
    def __init__(self, i, ten, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10):
        self.ma = f"HS{i+1:02d}"
        self.ten = ten
        self.tb = int((d1*2+ d2*2 + d3 + d4 + d5 + d6 +d7 + d8 + d9 + d10)/12*10+ 0.5)/10
        self.tt = "NONE"
        if self.tb >= 9: self.tt = "XUAT SAC"
        elif self.tb >= 8: self.tt = "GIOI"
        elif self.tb >= 7: self.tt = "KHA"
        elif self.tb >= 5: self.tt = "TB"
        else: self.tt = "YEU"
    def __str__(self):
        return self.ma + " " + self.ten + " " + f"{self.tb:.1f}" + " "+ self.tt
n = int(input())
ds = []
for i in range(n):
    ten = input()
    d1, d2, d3, d4, d5, d6, d7, d8, d9, d10 = map(float, input().split())
    ds.append(HS(i, ten, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10))
ds.sort(key=lambda x: (-x.tb, x.ma))
for hs in ds:
    print(hs)