n = int(input())
cnt = 0
ok = 0
for i in range(n):
    s = input().strip()
    if s:
        if ok == 1: cnt += 1
        else:
            print(s+ ": ", end="")
            ok = 1
    else:
        print(cnt)
        cnt = 0
        ok =0
print(cnt)