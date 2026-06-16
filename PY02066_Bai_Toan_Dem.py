import sys
data = sys.stdin.read().split()
n = int(data[0])
a = []
for idx in range(1, n+1):
    a.append(int(data[idx]))
set1 = set(a)
m = max(set1)
find = 0
for i in range(1, m+1):
    if i not in set1:
        find = 1
        print(i)
if find == 0:
    print("Excellent!")

