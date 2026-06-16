n = int(input())
a = []
kq = 0
for _ in range(n):
    a.append(input())
for i in range(n):
    cnt = a[i].count('C')
    kq += cnt * (cnt-1) // 2
for j in range(n):
    cnt = 0
    for i in range(n):
        if a[i][j] == 'C':
            cnt+=1
    kq += cnt * (cnt - 1) // 2
print(kq)
