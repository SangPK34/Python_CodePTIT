t = int(input())
for _ in range(t):
    s = input()
    a = ""
    b = ""
    seen = set()
    for c in s:
        if s.count(c)>1:
            if c not in seen:
                b+=c
                seen.add(c)
        else:
            a+=c
    if a == "": a = "NONE"
    if b == "": b = "NONE"
    print(a)
    print(b)