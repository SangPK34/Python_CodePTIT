import sys


def emit(s):
    s = " ".join(s.split())
    if not any(ch.isalnum() for ch in s):
        return
    s = s.lower()
    print(s[0].upper() + s[1:])


text = sys.stdin.read().replace("\ufeff", "")
cur = []
for ch in text:
    if ch in ".?!":
        emit("".join(cur))
        cur = []
    else:
        cur.append(ch)
emit("".join(cur))

