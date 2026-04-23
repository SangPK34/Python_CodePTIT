import sys


def solve():
    # Đọc data siêu tốc
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    idx = 0
    n_tokens = len(input_data)
    out = []

    while idx < n_tokens:
        n = int(input_data[idx])
        idx += 1

        # 1. Tạo mảng cộng dồn P
        P = [0.0] * (n + 1)
        curr = 0.0
        for i in range(n):
            curr += float(input_data[idx + i])
            P[i + 1] = curr
        idx += n

        # Hàm tính hệ số góc (đạo hàm)
        def slope(i, j):
            return (P[j] - P[i]) / (j - i)

        # 2. Xây dựng Bao lồi trên (Upper Hull) để tìm Max nhanh
        U = []
        for i in range(n + 1):
            # Cắt bỏ các điểm lõm, ép khuôn thành hình lồi (hệ số góc giảm dần)
            while len(U) >= 2 and slope(U[-2], U[-1]) <= slope(U[-1], i):
                U.pop()
            U.append(i)

        # Xây dựng Bao lồi dưới (Lower Hull) để tìm Min nhanh
        L = []
        for i in range(n + 1):
            # Cắt bỏ các điểm lõm, ép khuôn thành hình lồi (hệ số góc tăng dần)
            while len(L) >= 2 and slope(L[-2], L[-1]) >= slope(L[-1], i):
                L.pop()
            L.append(i)

        # Lưu sẵn hệ số góc của các đoạn trên Bao lồi
        slope_U = [slope(U[k], U[k + 1]) for k in range(len(U) - 1)]
        slope_L = [slope(L[k], L[k + 1]) for k in range(len(L) - 1)]

        # 3. Kỹ thuật Binary Search TRÊN Bao lồi (O(log N) thay vì O(N))
        def get_max_idx(x):
            low, high = 0, len(slope_U) - 1
            ans = len(slope_U)
            while low <= high:
                mid = (low + high) // 2
                if slope_U[mid] < x:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return U[ans]

        def get_min_idx(x):
            low, high = 0, len(slope_L) - 1
            ans = len(slope_L)
            while low <= high:
                mid = (low + high) // 2
                if slope_L[mid] > x:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return L[ans]

        # 4. Binary Search tìm X tối ưu (Thuật toán chính)
        l, r = -10000.0, 10000.0
        for _ in range(60):  # 60 vòng là ép sai số cực đoan luôn
            mid = (l + r) / 2.0

            i_max = get_max_idx(mid)
            i_min = get_min_idx(mid)

            # Cân bằng đỉnh và đáy
            if i_min < i_max:
                l = mid
            else:
                r = mid

        # 5. Chốt đáp án với độ chính xác 6 số thập phân
        best_x = (l + r) / 2.0
        i_max = get_max_idx(best_x)
        i_min = get_min_idx(best_x)
        ans = (P[i_max] - i_max * best_x) - (P[i_min] - i_min * best_x)

        out.append(f"{ans:.6f}")

    # In toàn bộ kết quả siêu tốc
    sys.stdout.write('\n'.join(out) + '\n')


if __name__ == '__main__':
    solve()