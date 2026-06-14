def check(s):
    if len(s)<6 or len(s)>12: return False
    thuong = False
    hoa = False
    so = False
    db = False
    for c in s:
        if 'a' <= c <= 'z' : thuong = True
        if 'A' <= c <= 'Z' : hoa = True
        if '0' <= c <= '9': so = True
        if c in "$!@#": db = True
    return thuong and hoa and so and db

s = list(input().split(','))
kq = []
for c in s:
    if check(c):
        kq.append(c)
if len(kq) == 0:
    print("INVALID PASSWORD")
else:
    print(",".join(kq))

