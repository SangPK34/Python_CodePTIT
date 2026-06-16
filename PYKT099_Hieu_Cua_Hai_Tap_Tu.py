import sys

sys.stdin = open("DATA1.in", "r")
ds1 = []
for s in sys.stdin:
    ds1 += s.strip().lower().split()

sys.stdin = open("DATA2.in", "r")
ds2 = []
for s in sys.stdin:
    ds2 += s.strip().lower().split()

set1 = set(ds1)
set2 = set(ds2)
print(*sorted(set1 - set2))
print(*sorted(set2 - set1))