f = open("CAU2.INP", "r")
n, k = map(int, f.readline().split())
a = list(map(int, f.readline().split()))
f.close()

a.sort(reverse=True)

tong = sum(a)
free = 0
for i in range(k - 1, n, k):
    free += a[i]

g = open("CAU2.OUT", "w")
g.write(str(tong - free))
g.close()
