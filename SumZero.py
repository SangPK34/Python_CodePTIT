import sys


def solve():
    def get_input():
        for line in sys.stdin:
            for word in line.split():
                yield word

    input_gen = get_input()

    try:
        t_str = next(input_gen)
    except StopIteration:
        return
    t = int(t_str)

    for _ in range(t):
        try:
            n = int(next(input_gen))
            a = []
            for _ in range(n):
                a.append(int(next(input_gen)))
        except StopIteration:
            break

        a.sort()
        s = 0

        for i in range(n - 2):

            if a[i] > 0:
                break

            x = a[i]
            l = i + 1
            r = n - 1

            while l < r:

                current_sum = x + a[l] + a[r]
                if current_sum == 0:
                    s += 1
                    l += 1
                elif current_sum < 0:
                    l += 1
                else:
                    r -= 1

        sys.stdout.write(str(s) + "\n")


if __name__ == "__main__":
    solve()