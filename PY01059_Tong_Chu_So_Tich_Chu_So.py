def check(s):
    C = 0
    L = 1
    ok = 1
    for i in range(len(s)):
        if i % 2 ==0:
            C += int(s[i])
        else:
            if int(s[i]) != 0:
                L *= int(s[i])
                ok = 0
    if ok == 1:
        L = 0
    print(str(C)+" "+str(L))

t = int(input())
for _ in range(t):
    s = input()
    check(s)