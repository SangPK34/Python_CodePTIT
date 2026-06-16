t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    while True:
        mid = 2 ** (n - 1)
        if k == mid:
            print(chr(ord('A') + n - 1))
            break
        elif k < mid:
            n -= 1
        else:
            k -= mid
            n -= 1

