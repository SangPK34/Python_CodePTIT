n = int(input())
a = []
while len(a) < n:
    a.extend(map(int, input().split()))
chan = []
le = []
loai = []
for x in a:
    if x % 2 == 0:
        chan.append(x)
        loai.append("c")
    else:
        le.append(x)
        loai.append("l")
chan.sort()
le.sort(reverse=True)
j = k = 0
res = ""
for c in loai:
    if c == "c":
        res += str(chan[j])+" "
        j += 1
    else:
        res += str(le[k])+" "
        k += 1
print(res.strip())