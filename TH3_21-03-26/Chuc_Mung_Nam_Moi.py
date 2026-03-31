import sys

a = sys.stdin.buffer.readline
n = int(a())
tap = set()
for _ in range(n):
    tap.add(a().rstrip(b'\n').decode())
print(len(tap))