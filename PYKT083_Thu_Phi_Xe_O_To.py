n = int(input())
ds = {}
for _ in range(n):
    s = input().split()
    if s[3] == "IN":
        if s[1] == "Xe_con" and s[2] == "5":
            dgia = 10000
        elif s[1] == "Xe_con" and s[2] == "7":
            dgia = 15000
        elif s[1] == "Xe_tai" and s[2] == "2":
            dgia = 20000
        elif s[1] == "Xe_khach" and s[2] == "29":
            dgia = 50000
        elif s[1] == "Xe_khach" and s[2] == "45":
            dgia = 70000
        if s[4] not in ds:
            ds[s[4]] = 0
        ds[s[4]] += dgia

for k, v in ds.items():
    print(k+": "+str(v))