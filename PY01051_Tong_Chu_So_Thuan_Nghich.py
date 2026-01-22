t = int(input())
for _ in range(t):
    s = input()
    A=0
    for i in s:
        A+=int(i)
    if str(A) == str(A)[::-1] and len(str(A))>1:
        print("YES")
    else :
        print("NO")