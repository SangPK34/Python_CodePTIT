import bisect
import math
import sys


def _all_collinear(xs, ys, n):
    i = 1
    x0 = xs[0]
    y0 = ys[0]
    while i < n and xs[i] == x0 and ys[i] == y0:
        i += 1
    if i == n:
        return True
    dx = xs[i] - x0
    dy = ys[i] - y0
    for j in range(i + 1, n):
        if dx * (ys[j] - y0) - dy * (xs[j] - x0) != 0:
            return False
    return True


def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    data[0] = data[0].lstrip(b"\xef\xbb\xbf")
    vals = list(map(int, data))

    t = vals[0]
    ptr = 1
    out = []

    pi = math.pi
    tau = 2.0 * pi
    eps = 1e-12
    atan2 = math.atan2
    br = bisect.bisect_right
    bl = bisect.bisect_left

    for _ in range(t):
        n = vals[ptr]
        ptr += 1
        k = vals[ptr]
        ptr += 1

        xs = [0] * n
        ys = [0] * n
        zs = [0] * n

        for i in range(n):
            x = vals[ptr]
            y = vals[ptr + 1]
            ptr += 2
            xs[i] = x
            ys[i] = y
            zs[i] = x * x + y * y

        if k > n - 3 or _all_collinear(xs, ys, n):
            out.append("NO")
            continue

        ok = False

        for i in range(n - 1):
            if ok:
                break

            xi = xs[i]
            yi = ys[i]
            zi = zs[i]

            for j in range(i + 1, n):
                ux = xs[j] - xi
                uy = ys[j] - yi
                if ux == 0 and uy == 0:
                    continue

                uz = zs[j] - zi
                v1x = -uy
                v1y = ux
                v2x = -uz * ux
                v2y = -uz * uy
                v2z = ux * ux + uy * uy

                arr = []
                has_nonzero = False
                for m in range(n):
                    if m == i or m == j:
                        continue
                    wx = xs[m] - xi
                    wy = ys[m] - yi
                    wz = zs[m] - zi

                    orient_ijm = v1x * wx + v1y * wy
                    if orient_ijm != 0:
                        has_nonzero = True
                    py = v2x * wx + v2y * wy + v2z * wz
                    arr.append((atan2(py, orient_ijm), orient_ijm))

                if not has_nonzero:
                    continue

                arr.sort(key=lambda x: x[0])
                r = len(arr)
                ang = [a for a, _ in arr]
                ext = ang + [a + tau for a in ang]

                for p, (theta, orient_ijm) in enumerate(arr):
                    if orient_ijm == 0:
                        continue

                    l = br(ext, theta + eps, p + 1, p + r)
                    mid = bl(ext, theta + pi - eps, l, p + r + 1)
                    pos = mid - l

                    l2 = br(ext, theta + pi + eps, mid, p + r + 1)
                    r2 = bl(ext, theta + tau - eps, l2, p + r + 1)
                    neg = r2 - l2

                    inside = neg if orient_ijm > 0 else pos
                    if inside == k:
                        ok = True
                        break

                if ok:
                    break

        out.append("YES" if ok else "NO")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
