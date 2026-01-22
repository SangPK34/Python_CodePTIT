def check(s):
    if len(s) % 2 ==1:
        return False
    r = s[::-1]
    for i in range(0, len(r)):
        if int(s[i]) % 2==1:
            return False
        if r[i] != s[i]:
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(2, n, 2):
        if check(str(i)):
            print(i, end=" ")
    print("")