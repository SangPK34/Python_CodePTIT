def check(s):
    C = 1
    L =0
    for i in range(len(s)):
        if i% 2 ==0:
            if int(s[i]) != 0: C *= int(s[i])
        else:
            L += int(s[i])
    print(str(C) + " " + str(L))

t = int(input())
for _ in range(t):
    s = input()
    check(s)