import sys


def giai():
    dong = sys.stdin.read().splitlines()
    if not dong:
        return
    n = int(dong[0].strip())
    tho = dong[1:1 + n]
    dem = [len(s.split()) for s in tho]

    kt2 = [False] * (n + 1)
    for i in range(n - 3):
        if dem[i] == 7 and dem[i + 1] == 7 and dem[i + 2] == 7 and dem[i + 3] == 7:
            kt2[i] = True

    ds1 = [[] for _ in range(n + 1)]
    for i in range(n):
        j = i
        while j + 1 < n and dem[j] == 6 and dem[j + 1] == 8:
            ds1[i].append(j + 2)
            j += 2

    dp = [[False, False] for _ in range(n + 1)]
    chon = [[None, None] for _ in range(n + 1)]
    dp[n][0] = True
    dp[n][1] = True

    for i in range(n - 1, -1, -1):
        if kt2[i] and dp[i + 4][0]:
            dp[i][0] = True
            chon[i][0] = (2, i + 4, 0)
        for e in ds1[i]:
            if dp[e][1]:
                dp[i][0] = True
                chon[i][0] = (1, e, 1)
                break

        if kt2[i] and dp[i + 4][0]:
            dp[i][1] = True
            chon[i][1] = (2, i + 4, 0)

    if not dp[0][0]:
        return

    kq = []
    i = 0
    tr = 0
    while i < n:
        loai, ni, ntr = chon[i][tr]
        kq.append(loai)
        i = ni
        tr = ntr

    out = [str(len(kq))]
    out.extend(map(str, kq))
    sys.stdout.write('\n'.join(out))


if __name__ == '__main__':
    giai()
