import sys

a = sys.stdin.buffer.read().split()
print('\n'.join('YES' if s[0] == s[-1] else 'NO' for s in a[1:]))