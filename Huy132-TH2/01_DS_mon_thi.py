class MonHoc:
    def __init__(self, ma, ten, hinh_thuc):
        self.ma = ma
        self.ten = ten
        self.hinh_thuc = hinh_thuc

    def __str__(self):
        return f"{self.ma} {self.ten} {self.hinh_thuc}"


a = []
for _ in range(int(input())):
    ma = input().strip()
    ten = input().strip()
    hinh_thuc = input().strip()
    a.append(MonHoc(ma, ten, hinh_thuc))

a.sort(key=lambda x: x.ma)

for x in a:
    print(x)