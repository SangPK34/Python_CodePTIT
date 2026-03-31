import sys

def dao_so(n):
    return int(str(n)[::-1])

def sang_nt(m):
    nt = [True] * (m + 1)
    nt[0] = nt[1] = False
    for i in range(2, int(m ** 0.5) + 1):
        if nt[i]:
            for j in range(i * i, m + 1, i):
                nt[j] = False
    return nt

def xu_ly(n, nt):
    kq = []
    for i in range(2, n):
        if nt[i]:
            j = dao_so(i)
            if j != i and j < n and nt[j] and i < j:
                kq.append(str(i))
                kq.append(str(j))
    return ' '.join(kq)

du_lieu = sys.stdin.read().strip().split()
if du_lieu:
    t = int(du_lieu[0])
    ds_n = list(map(int, du_lieu[1:1 + t]))
    mx = max(ds_n)
    nt = sang_nt(mx)
    print('\n'.join(xu_ly(n, nt) for n in ds_n))