n = int(input())
a = []
kq = []
cnt = 0
for i in range(n):
    line = input().split()
    a.append(len(line))
idx = 0
while idx<n:
    if a[idx] == 6:
        while a[idx] == 6:
            idx += 2
            if idx == n:break
        kq.append(1)
    else:
        while a[idx] == 7:
            idx += 4
            kq.append(2)
            if idx == n: break
print((len(kq)))
for k in kq:
    print(k)

