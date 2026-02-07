f = open("CAU1.INP", "r")
n, k = map(int, f.read().split())
f.close()

d = [0] * (n + 1)
for i in range(1, n + 1):
    for j in range(i, n + 1, i):
        d[j] += 1

kq = 0
for x in range(1, n + 1):
    if d[x] == k:
        kq += 1

g = open("CAU1.OUT", "w")
g.write(str(kq))
g.close()
