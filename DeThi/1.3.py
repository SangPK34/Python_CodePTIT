t = int(input())
for _ in range(t):
    s = input()
    chan = 0.0
    le = 1.0
    for c in s[1::2]:
        chan += int(c)
    for c in s[0::2]:
        if c!='0': le *= int(c)
    print("INVALID" if chan == 0 else f"{le/chan:.6f}")