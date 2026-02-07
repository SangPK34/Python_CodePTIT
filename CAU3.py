f = open("CAU3.INP", "r")
n = int(f.readline().strip())
arr = [f.readline().strip() for _ in range(n)]
s = f.readline().strip()
f.close()

d = len(s)

for k in range(d):
    ok = False
    need = s[k]
    for i in range(n):
        if arr[i][k] == need:
            ok = True
            break
    if not ok:
        g = open("CAU3.OUT", "w")
        g.write("-1")
        g.close()
        raise SystemExit

kq = d
for i in range(n):
    khac = 0
    si = arr[i]
    for k in range(d):
        if si[k] != s[k]:
            khac += 1
    if khac < kq:
        kq = khac

g = open("CAU3.OUT", "w")
g.write(str(kq))
g.close()
