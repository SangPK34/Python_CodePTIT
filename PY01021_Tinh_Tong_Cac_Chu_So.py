t = int(input())
for _ in range(t):
    s = input()
    A = 0
    res = []
    for c in s:
        if c.isdigit():
            A += int(c)
        else:
            res.append(c)
    res.sort()
    res.append(str(A))
    print("".join(res))
