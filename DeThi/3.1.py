import math
t = int(input())
for _ in range(t):
    x = list(map(float, input().split()))
    y = list(map(float, input().split()))
    if len(x) != len(y):
        print("INVALID")
        continue
    tong=0.0
    for i in range(len(x)):
        tong += (x[i]-y[i])**2
    kq = math.sqrt(tong)
    print(f"{kq:.5f}")