import math

class PS:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    def rutgon(self):
        k = math.gcd(self.tu, self.mau)
        self.tu //= k
        self.mau //= k
        return self

    def cong(self, b):
        tu = self.tu * b.mau + self.mau * b.tu
        mau = self.mau * b.mau
        return PS(tu, mau).rutgon()

    def __str__(self):
        return f"{self.tu}/{self.mau}"


tu1, mau1, tu2, mau2 = map(int, input().split())

p1 = PS(tu1, mau1)
p2 = PS(tu2, mau2)

print(p1.cong(p2))