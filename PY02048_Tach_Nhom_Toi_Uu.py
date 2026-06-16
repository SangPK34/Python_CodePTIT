import sys
data = sys.stdin.read().split()
n, k = map(int,data[:2])
idx = 2
a = sorted(map(int, data[idx:idx+n]))
kq = 1
for i in range(1,n):
    if a[i] - a[i-1] > k:
        kq += 1
print(kq)





