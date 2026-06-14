from datetime import datetime, timedelta


class NV:
    def __init__(self, ma, ten, vao, ra):
        self.ma = ma
        self.ten = ten
        self.vao = vao
        self.ra = ra
        timera = datetime.strptime(ra, "%H:%M")
        timevao = datetime.strptime(vao, "%H:%M")
        self.diff = timera - timevao - timedelta(hours=1)
        tongphut = int(self.diff.total_seconds()//60)
        gio = tongphut // 60
        phut = tongphut % 60
        self.giolam = f"{gio} gio {phut} phut"

        if self.diff >= timedelta(hours=8):
            self.tt = "DU"
        else:
            self.tt = "THIEU"

    def __str__(self):
        return f"{self.ma} {self.ten} {self.giolam} {self.tt}"

n = int(input())
ds= []
for i in range(n):
    ma = input()
    ten = input()
    vao = input()
    ra = input()
    ds.append(NV(ma, ten, vao, ra))
ds.sort(key = lambda x: -x.diff)
for i in ds:
    print(i)

