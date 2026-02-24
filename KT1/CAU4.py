f = open("CAU4.INP", "r")
sh, sc = map(int, f.readline().split())
dai, rong, cao = map(int, f.readline().split())
bdo = []
for i in range(sh):
    bdo.append(list(map(int, f.readline().split())))
f.close()

phi = []
for i in range(sh):
    dong = []
    for j in range(sc):
        dong.append(abs(bdo[i][j] - cao))
    phi.append(dong)

tong = []
for i in range(sh + 1):
    tong.append([0] * (sc + 1))

for i in range(1, sh + 1):
    tam = 0
    for j in range(1, sc + 1):
        tam += phi[i - 1][j - 1]
        tong[i][j] = tong[i - 1][j] + tam

def lay(x1, y1, x2, y2):
    return tong[x2 + 1][y2 + 1] - tong[x1][y2 + 1] - tong[x2 + 1][y1] + tong[x1][y1]

vo_cuc = 10**30
kq = vo_cuc

def thu(r, d):
    global kq
    if r > sh or d > sc:
        return
    for i in range(sh - r + 1):
        for j in range(sc - d + 1):
            gt = lay(i, j, i + r - 1, j + d - 1)
            if gt < kq:
                kq = gt

thu(rong, dai)
thu(dai, rong)

g = open("CAU4.OUT", "w")
g.write(str(-1 if kq == vo_cuc else kq))
g.close()
