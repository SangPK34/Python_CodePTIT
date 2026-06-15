class TS:
    def __init__(self, i, ten, lt, th):
        self.ma = f"TS0{i+1}"
        self.ten = ten
        while lt > 10:
            lt /= 10
        while th > 10:
            th /= 10
        self.tb = 1/2*(lt+th)
        if self.tb < 5: self.tt = "TRUOT"
        elif self.tb <8: self.tt = "CAN NHAC"
        elif self.tb <9.5: self.tt = "DAT"
        else: self.tt = "XUAT SAC"
    def __str__(self):
        return self.ma + " " + self.ten + " " + f"{self.tb:.2f}" + " " + self.tt
n = int(input())
ds = []
for i in range(n):
    ten = input()
    lt = float(input())
    th = float(input())
    ds.append(TS(i, ten, lt, th))
ds.sort(key = lambda x: -x.tb)
for ts in ds:
    print(ts)
