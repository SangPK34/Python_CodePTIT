t = int(input())
for _ in range(t):
    s = input()
    if int(s)%7==0:
        print(int(s))
        continue
    ok =0
    for i in range(1000):
        s = str(int(s) + int(s[::-1]))
        if int(s) % 7==0:
            ok = 1
            break
    if ok == 1:
        print(int(s))
    else :
        print("-1")