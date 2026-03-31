while True:
    a = list(map(int, input().split()))
    if a == [0, 0, 0, 0]:
        break
    d = 0
    while len(set(a)) > 1:
        a = [abs(a[i] - a[(i + 1) % 4]) for i in range(4)]
        d += 1
    print(d)