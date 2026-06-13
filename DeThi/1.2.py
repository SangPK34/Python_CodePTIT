t = int(input())
for _ in range(t):
    n = int(input())
    kq = 0.0
    if n % 2 == 0:
        start = 2
    else:
        start = 1
    cnt = 0
    for i in range(start, n+1, 2):
        cnt +=1
        if cnt %2 == 1:
            kq += 1/i
        else:
            kq -= 1/i
    print(f"{kq:.5f}")
