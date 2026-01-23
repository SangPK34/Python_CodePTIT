n = int(input())
set1 = set(map(int, input().split()))
a = sorted(list(set1))
i = 1
for x in a:
    if x<i: continue
    if x == i: i+=1
    else:
        break
print(i)