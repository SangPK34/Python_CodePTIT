n = int(input())
a = []
while len(a) < n:
    a.extend(map(int, input().split()))
cl=[]
c=[]
l=[]
for x in a:
    if x%2==0:
        cl.append("c")
        c.append(x)
    else:
        cl.append("l")
        l.append(x)
c.sort()
l.sort(reverse=True)
C = 0
L = 0
res = []
for x in cl:
    if x == "c":
        res.append(str(c[C]))
        C += 1
    else:
        res.append(str(l[L]))
        L += 1
print(" ".join(res))