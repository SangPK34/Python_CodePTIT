import math

t = int(input())
for _ in range(t):
    ok=1
    s1 = input()
    s2 = s1[::-1]
    for i in range(0, len(s1)-1):
        if (abs(ord(s1[i]) - ord(s1[i-1])) != abs(ord(s2[i]) - ord(s2[i-1]))):
            print("NO")
            ok=0
            break
    if ok==1:
        print("YES")
