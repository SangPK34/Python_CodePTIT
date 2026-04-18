import sys


class ThiSinh:
    def __init__(self, ho_ten, ngay_sinh, d1, d2, d3):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.tong = d1 + d2 + d3


lines = [line.rstrip("\n") for line in sys.stdin.read().replace("\ufeff", "").splitlines()]
if lines:
    name = lines[0].strip()
    dob = lines[1].strip()
    d1 = float(lines[2].strip())
    d2 = float(lines[3].strip())
    d3 = float(lines[4].strip())

    ts = ThiSinh(name, dob, d1, d2, d3)
    print(f"{ts.ho_ten} {ts.ngay_sinh} {ts.tong:.1f}")

