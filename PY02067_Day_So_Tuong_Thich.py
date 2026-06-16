n = int(input())
a = list(map(int, input().split()))
kq = 10 **18
for k in range(1, min(a)+1):
    find = True
    tong = 0
    for x in a:
        b = x //(k+1) +1
        if x // b != k:
            find = False
            break
        tong += b
    if find:
        kq = min(kq, tong)
print(kq)