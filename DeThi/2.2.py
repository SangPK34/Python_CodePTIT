t = int(input())
for _ in range(t):
    s = input()
    arr = s.split('1')
    leng = []
    for c in arr:
        leng.append(len(c))
    print(max(leng))