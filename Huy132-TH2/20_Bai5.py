MOD = 10**9 + 7

n, m = map(int, input().split())
a = list(map(int, input().split()))

s = m - sum(a)

if s < 0:
    print(0)
else:
    N = s + n - 1
    K = n - 1

    fact = [1] * (N + 1)
    for i in range(1, N + 1):
        fact[i] = fact[i - 1] * i % MOD

    inv_fact = [1] * (N + 1)
    inv_fact[N] = pow(fact[N], MOD - 2, MOD)
    for i in range(N, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD

    ans = fact[N] * inv_fact[K] % MOD * inv_fact[N - K] % MOD
    print(ans)