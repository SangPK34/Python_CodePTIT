t = int(input())
for _ in range(t):
    s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n, b = map(int, input().split())
    res = ""
    while n > 0:
        res = s[n % b] + res
        n //= b
    print(res)
