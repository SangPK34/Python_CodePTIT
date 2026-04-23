import sys
from functools import lru_cache


def solve():
    # Đọc hết input một cục cho lẹ, bài này 10000 test case đọc từng dòng là niệm
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    T = int(input_data[0])
    out = []

    # Memoize phi(M) để khỏi tính lại mấy M trùng nhau
    @lru_cache(None)
    def get_phi(n):
        res = n
        if n % 2 == 0:
            while n % 2 == 0: n //= 2
            res -= res // 2
        if n % 3 == 0:
            while n % 3 == 0: n //= 3
            res -= res // 3
        p = 5
        # Bước nhảy 6 để skip nhanh các số chẵn và chia hết cho 3
        while p * p <= n:
            if n % p == 0:
                while n % p == 0: n //= p
                res -= res // p
            if n % (p + 2) == 0:
                while n % (p + 2) == 0: n //= (p + 2)
                res -= res // (p + 2)
            p += 6
        if n > 1:
            res -= res // n
        return res

    idx = 1
    for _ in range(T):
        a = int(input_data[idx])
        b = int(input_data[idx + 1])
        c = int(input_data[idx + 2])
        d = int(input_data[idx + 3])
        M = int(input_data[idx + 4])
        idx += 5

        if M == 1:
            out.append("0")
            continue

        P = get_phi(M)

        if b == 0:
            E = 0
        elif c == 0:
            cd = 1 if d == 0 else 0
            val = b * cd
            E = val if val < P else val % P + P
        elif c == 1:
            val = b
            E = val if val < P else val % P + P
        else:
            # Ngưỡng an toàn 24 vì 2^24 > 10^7 >= P
            if d >= 24:
                cd_mod = pow(c, d, P)
                E = (b * cd_mod) % P + P
            else:
                val = b * (c ** d)
                E = val if val < P else val % P + P

        ans = pow(a, E, M)
        out.append(str(ans))

    sys.stdout.write('\n'.join(out) + '\n')


if __name__ == '__main__':
    solve()