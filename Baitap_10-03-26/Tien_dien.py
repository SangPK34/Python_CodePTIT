tien = []
# nhập tiền điện 12 tháng
for i in range(12):
    x = int(input())
    tien.append(x)
tong = sum(tien)
trung_binh = tong / 12

print("Tong tien dien:", tong)
print("Tien dien trung binh:", trung_binh)

print("Cac thang co tien dien lon hon trung binh:")
for i in range(12):
    if tien[i] > trung_binh:
        print("Thang", i+1)