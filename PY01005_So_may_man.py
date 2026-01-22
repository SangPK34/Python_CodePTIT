t = int(input())
while t>0:
    s = list(input().strip())
    ok = 1
    for i in s:
        if i != '4' and i != '7':
            ok = 0
            break
    if ok==1: print('YES')
    else: print('NO')
    t-=1