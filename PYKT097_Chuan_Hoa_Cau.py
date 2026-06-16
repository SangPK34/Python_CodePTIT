# Chuong trinh Dao Tao CLC nganh CNTT duoc Thiet     Ke theo chuan quoc te.
# co 03 chuyen nganh la: Cong  nghe phan mem, Tri tue nhan tao va An toan thong tin
# muc tieu cua chuong trinh la trang bi cho sinh vien cac ky nang nghe nghiep
# moi    CAC BAN danG ky     thaM giA !
import sys

data = sys.stdin.read().splitlines()
res = []
for line in data:
    line = line.strip()
    if line == "":
        continue
    line = " ".join(line.lower().split())
    line = line[0].upper() + line[1:]
    if line[-1] not in '.!?':
        line += "."
    else:
        for c in ".!?":
            line = line.replace(" "+c, c)
    res.append(line)
for s in res:
    print(s)