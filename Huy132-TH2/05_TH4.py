import sys


def main():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    k = int(data[1])

    count = sum(1 for i in range(2, n + 2) if int(data[i]) % k == 0)

    print(count)


if __name__ == '__main__':
    main()