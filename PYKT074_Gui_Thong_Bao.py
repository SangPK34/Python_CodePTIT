import textwrap
n = int(input())
for _ in range(n):
    s = input()
    # res = ""
    # s = input().split()
    # for i in range(len(s)):
    #     if len(res)+len(s[i]) <=100:
    #         res += s[i] + " "
    #     else: break
    # print(res.strip())
    print(textwrap.shorten(s, 100, placeholder=""))