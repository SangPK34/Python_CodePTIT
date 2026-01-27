def conv(a, b):
    s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if a == 0: return "0"
    res = ""
    while a > 0:
        res = s[a%b] + res
        a //= b
    return res

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(conv(a, b))