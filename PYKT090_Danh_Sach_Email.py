import sys
sys.stdin = open("CONTACT.in", "r")

ds = set()
for line in sys.stdin:
    line = line.strip()
    if line == "": continue
    else:
        ds.add(line.lower())
a = list(sorted(ds))
for i in a:
    print(i)