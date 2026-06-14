t = int(input())
for _ in range(t):
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    p = int(input())
    if len(x) != len(y):
        print("INVALID")
        continue
    tong = 0.0
    for i in range(len(x)):
        tong += (abs(x[i]- y[i]))**p
    kq = tong ** (1/p)
    print(f"{kq:.5f}")