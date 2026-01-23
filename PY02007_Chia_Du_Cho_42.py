n = 10
import sys
a = list(map(int, sys.stdin.read().split()))
set1 = set()
for i in a:
    set1.add(i%42)
print(len(set1))
