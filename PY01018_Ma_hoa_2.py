while True:
    line = input().strip()
    part = line.split()
    k = int(part[0])
    if k == 0:
        break
    s = part[1]
    p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
    res = ""
    for c in s:
        n = p.find(c)
        res += p[(n + k) % 28]
    print(res[::-1])
