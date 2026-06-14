n = int(input())
a = input().split()
x = input()
kq = []
for i in range(len(a)):
    if x == a[i]:
        kq.append(str(i))
if len(kq) == 0:
    print("-1")
else:
    print(", ".join(kq))
