import sys

a = list(map(int, sys.stdin.buffer.read().split()))
kq = []
for i in range(1, len(a), 2):
    d, m = a[i], a[i + 1]
    if (m == 3 and d >= 21) or (m == 4 and d <= 19): kq.append('Bach Duong')
    elif (m == 4 and d >= 20) or (m == 5 and d <= 20): kq.append('Kim Nguu')
    elif (m == 5 and d >= 21) or (m == 6 and d <= 20): kq.append('Song Tu')
    elif (m == 6 and d >= 21) or (m == 7 and d <= 22): kq.append('Cu Giai')
    elif (m == 7 and d >= 23) or (m == 8 and d <= 22): kq.append('Su Tu')
    elif (m == 8 and d >= 23) or (m == 9 and d <= 22): kq.append('Xu Nu')
    elif (m == 9 and d >= 23) or (m == 10 and d <= 22): kq.append('Thien Binh')
    elif (m == 10 and d >= 23) or (m == 11 and d <= 22): kq.append('Thien Yet')
    elif (m == 11 and d >= 23) or (m == 12 and d <= 21): kq.append('Nhan Ma')
    elif (m == 12 and d >= 22) or (m == 1 and d <= 19): kq.append('Ma Ket')
    elif (m == 1 and d >= 20) or (m == 2 and d <= 18): kq.append('Bao Binh')
    else: kq.append('Song Ngu')
print('\n'.join(kq))