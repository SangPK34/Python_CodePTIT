class ThiSinh:
    def __init__(self, stt, ho_ten, diem_ly_thuyet, diem_thuc_hanh):
        self.ma = f'TS0{stt}'
        self.ten = ho_ten
        self.diem_tb = (
            (diem_ly_thuyet if diem_ly_thuyet <= 10 else diem_ly_thuyet / 10) +
            (diem_thuc_hanh if diem_thuc_hanh <= 10 else diem_thuc_hanh / 10)
        ) / 2

        if self.diem_tb >= 9.5:
            self.xep_hang = 'XUAT SAC'
        elif self.diem_tb >= 8:
            self.xep_hang = 'DAT'
        elif self.diem_tb >= 5:
            self.xep_hang = 'CAN NHAC'
        else:
            self.xep_hang = 'TRUOT'

    def __str__(self):
        return self.ma + ' ' + self.ten + ' ' + f'{self.diem_tb:.2f}' + ' ' + self.xep_hang


ds_thi_sinh = []
for vi_tri in range(int(input())):
    ds_thi_sinh.append(
        ThiSinh(
            vi_tri + 1,
            input(),
            float(input()),
            float(input())
        )
    )

for thi_sinh in sorted(ds_thi_sinh, key=lambda x: -x.diem_tb):
    print(thi_sinh)