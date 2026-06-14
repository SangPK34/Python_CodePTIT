def check(s):
    while(len(s)>1):
        tong = 0
        for c in s:
            tong += int(c)**2
        s = str(tong)
    if s == "1": return True
    else: return False

s = input()
print("YES" if check(s) else "NO")