from collections import deque

n = 50
q = deque()
q.append("6")
q.append("8")
res = []
while(len(q) < n):
    s = q.popleft()
    res.append(s)
    q.append(s+"6")
    q.append(s+"8")
print(*res)