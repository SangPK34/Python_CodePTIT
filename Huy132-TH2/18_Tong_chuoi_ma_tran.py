import sys


def mul(X, Y, n):
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if X[i][k]:
                for j in range(n):
                    res[i][j] = (res[i][j] + X[i][k] * Y[k][j]) % 10
    return res


def add(X, Y, n):
    return [[(X[i][j] + Y[i][j]) % 10 for j in range(n)] for i in range(n)]


def pow_sum(A, k, n):
    if k == 1:
        return A, A
    hp, hs = pow_sum(A, k // 2, n)
    fp = mul(hp, hp, n)
    se = add(hs, mul(hp, hs, n), n)
    if k % 2 == 0:
        return fp, se
    else:
        fpo = mul(fp, A, n)
        return fpo, add(se, fpo, n)


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    k = int(input_data[1])

    A = []
    idx = 2
    for _ in range(n):
        A.append([int(x) % 10 for x in input_data[idx:idx + n]])
        idx += n

    _, res = pow_sum(A, k, n)

    for row in res:
        sys.stdout.write(" ".join(map(str, row)) + "\n")


if __name__ == '__main__':
    main()