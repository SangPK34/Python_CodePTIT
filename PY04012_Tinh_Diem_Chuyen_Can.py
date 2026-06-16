class SV:
    def __init__(self, ma, ten, lop):
        self.ma = ma
        self.ten = ten
        self.lop = lop
    def __str__(self):
        return f"{self.ma} {self.ten} {self.lop}"

n = int(input())
ds = []
for _ in range(n):
    ds.append(SV(input(), input(), input()))
dsdiem = {}
for _ in range(n):
    ma, dd = input().split()
    diem = 10 - dd.count('v') * 2 - dd.count('m')
    if diem < 0:
        diem = 0
    if diem == 0:
        dsdiem[ma] = f"{diem} KDDK"
    else:
        dsdiem[ma] = str(diem)
for sv in ds:
    print(sv, dsdiem[sv.ma])