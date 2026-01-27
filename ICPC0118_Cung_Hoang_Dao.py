def cung(day, month):
    if (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Ma Ket"
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Bao Binh"
    if (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Song Ngu"
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Bach Duong"
    if (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Kim Nguu"
    if (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Song Tu"
    if (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cu Giai"
    if (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Su Tu"
    if (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Xu Nu"
    if (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Thien Binh"
    if (month == 10 and day >= 23) or (month == 11 and day <= 22):
        return "Thien Yet"
    if (month == 11 and day >= 23) or (month == 12 and day <= 21):
        return "Nhan Ma"


t = int(input())
for _ in range(t):
    d, m = map(int, input().split())
    print(cung(d, m))