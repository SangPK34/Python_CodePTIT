import sys, re
s = sys.stdin.read()
s = " ".join(s.lower().split())
cau = re.split("[!.?]", s)
for x in cau:
    x = x.strip()
    if x:
        print(x[0].upper() + x[1:])



