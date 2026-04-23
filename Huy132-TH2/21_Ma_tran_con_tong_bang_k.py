import sys


def _count_exact_k(rows_pos, row_ones, r, c, k):
    ans = 0
    km1 = k - 1
    threshold = (c * 3) // 10
    cols = range(c)

    for top in range(r):
        col = [0] * c
        alive = c
        strip_total = 0
        parent = list(range(c + 1))

        for bottom in range(top, r):
            row_pos = rows_pos[bottom]
            strip_total += row_ones[bottom]

            for x in row_pos:
                old = col[x]
                if old <= k:
                    nv = old + 1
                    col[x] = nv
                    if nv == k + 1:
                        alive -= 1
                        y = x + 1
                        while parent[y] != y:
                            parent[y] = parent[parent[y]]
                            y = parent[y]
                        parent[x] = y

            # If every column already exceeds K, deeper bottoms cannot contribute anymore.
            if alive == 0:
                break

            # If total ones in this strip is still < K, no rectangle can reach K yet.
            if strip_total < k:
                continue

            # Count subarrays with sum exactly K in one pass:
            # exactly(K) = at_most(K) - at_most(K-1)
            add = 0
            col_local = col

            if alive >= threshold:
                l1 = 0
                l2 = 0
                s1 = 0
                s2 = 0

                for x in cols:
                    v = col_local[x]
                    if v > k:
                        l1 = x + 1
                        l2 = x + 1
                        s1 = 0
                        s2 = 0
                        continue

                    s1 += v
                    while s1 > k:
                        s1 -= col_local[l1]
                        l1 += 1

                    s2 += v
                    while s2 > km1:
                        s2 -= col_local[l2]
                        l2 += 1

                    add += l2 - l1
            else:
                x = 0
                while parent[x] != x:
                    parent[x] = parent[parent[x]]
                    x = parent[x]

                prev = -2
                l1 = 0
                l2 = 0
                s1 = 0
                s2 = 0

                while x < c:
                    if x != prev + 1:
                        l1 = x
                        l2 = x
                        s1 = 0
                        s2 = 0

                    v = col_local[x]

                    s1 += v
                    while s1 > k:
                        s1 -= col_local[l1]
                        l1 += 1

                    s2 += v
                    while s2 > km1:
                        s2 -= col_local[l2]
                        l2 += 1

                    add += l2 - l1
                    prev = x
                    nx = x + 1
                    while parent[nx] != nx:
                        parent[nx] = parent[parent[nx]]
                        nx = parent[nx]
                    x = nx

            ans += add

    return ans


def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    data[0] = data[0].lstrip(b"\xef\xbb\xbf")

    t = int(data[0])
    ptr = 1
    out = []

    for _ in range(t):
        n = int(data[ptr])
        ptr += 1
        m = int(data[ptr])
        ptr += 1
        k = int(data[ptr])
        ptr += 1

        raw_rows = data[ptr:ptr + n]
        ptr += n

        total_ones = 0
        for b in raw_rows:
            total_ones += b.count(49)  # ord('1')

        if total_ones < k:
            out.append("0")
            continue

        if n <= m:
            rows_pos = []
            row_ones = []
            for b in raw_rows:
                pos = []
                append_pos = pos.append
                for j, ch in enumerate(b):
                    if ch == 49:
                        append_pos(j)
                rows_pos.append(pos)
                row_ones.append(len(pos))

            ans = _count_exact_k(rows_pos, row_ones, n, m, k)
        else:
            # Transpose to keep squared dimension as small as possible.
            rows_pos = [[] for _ in range(m)]
            for i, b in enumerate(raw_rows):
                for j in range(m):
                    if b[j] == 49:
                        rows_pos[j].append(i)

            row_ones = [len(pos) for pos in rows_pos]
            ans = _count_exact_k(rows_pos, row_ones, m, n, k)

        out.append(str(ans))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()