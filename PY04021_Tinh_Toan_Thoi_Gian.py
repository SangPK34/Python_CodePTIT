def tomin(s):
    return int(s[:2])*60 + int(s[3:])
class KH:
    def __init__(self, ma, ten, vao, ra):
        self.ma = ma
        self.ten = ten
        self.vao = vao
        self.ra = ra
        self.phut = tomin(ra) - tomin(vao)
        self.tgian = f"{self.phut//60} gio {self.phut %60} phut"
    def __str__(self):
        return self.ma + " " + self.ten + " " +self.tgian
n = int(input())
ds = []
for i in range(n):
    ds.append(KH(input(), input(), input(), input()))
ds.sort(key = lambda x: -x.phut)
for kh in ds:
    print(kh)