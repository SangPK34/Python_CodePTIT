import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    N = int(input_data[0])
    S = input_data[1]
    MOD = 10 ** 9 + 7

    min_len = [0] * (1 << 20)
    for i in range(1, 1 << 20):
        lsb = i & -i
        val = lsb.bit_length()
        min_len[i] = min_len[i ^ lsb] + val.bit_length()

    rem = [0] * (N + 1)
    for i in range(N):
        for j in range(i + 1, N + 1):
            val = int(S[i:j], 2)
            if 1 <= val <= 20:
                rem[i] |= (1 << (val - 1))
    for i in range(N - 1, -1, -1):
        rem[i] |= rem[i + 1]

    dp = [{} for _ in range(N + 1)]

    for j in range(1, N + 1):
        for i in range(j - 1, -1, -1):
            val = int(S[i:j], 2)
            if val == 0 or val > 20:
                continue

            bit = 1 << (val - 1)
            req = (1 << bit.bit_length()) - 1
            missing = req ^ bit

            if (missing & ~rem[j]) == 0 and min_len[missing] <= N - j:
                dp[j][bit] = (dp[j].get(bit, 0) + 1) % MOD

            for mask, count in dp[i].items():
                nmask = mask | bit
                req = (1 << nmask.bit_length()) - 1
                missing = req ^ nmask
                if (missing & ~rem[j]) == 0 and min_len[missing] <= N - j:
                    dp[j][nmask] = (dp[j].get(nmask, 0) + count) % MOD

    ans = 0
    valid_masks = [(1 << m) - 1 for m in range(1, 21)]

    for j in range(1, N + 1):
        for mask in valid_masks:
            if mask in dp[j]:
                ans = (ans + dp[j][mask]) % MOD

    print(ans)


if __name__ == '__main__':
    solve()