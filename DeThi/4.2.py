class SV:
    def __init__(self, ten, ns, d1, d2, d3):
        self.ten = " ".join(ten.split()).title()
        d, m, y = map(int, ns.split('/'))
        self.ns = f"{d:02d}/{m:02d}/{y}"
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        dmin = min(d1, d2, d3)
        self.tb = (dmin*2 + (d1+ d2 +d3 -dmin))/4
    def __str__(self):
        return f"{self.ten} {self.ns} {self.tb:.1f}"

n = int(input())
ds = []
for i in range(n):
    ten = input()
    ns = input()
    d1 = float(input())
    d2 = float(input())
    d3 = float(input())
    ds.append(SV(ten, ns, d1, d2, d3))

ds.sort(key = lambda x: -x.tb)
for i in ds:
    print(i)
