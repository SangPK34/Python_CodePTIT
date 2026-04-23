import sys

n = sys.stdin.readline().strip()

kq = []
i = len(n)
while i > 0:
    j = i - 3
    if j < 0:
        j = 0
    kq.append(str(int(n[j:i], 2)))
    i = j

sys.stdout.write(''.join(reversed(kq)))
