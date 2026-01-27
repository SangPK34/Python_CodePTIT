t = int(input())
for _ in range(t):
    set1 = set()
    s = input()
    a = ""
    for c in s:
        if c.isdigit():
            a += c
        else:
            if a:
                set1.add(int(a))
                a = ""
    if a:
        set1.add(int(a))
    print(min(set1))