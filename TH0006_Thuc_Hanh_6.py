import heapq

n = int(input())
a = list(map(int, input().split()))

heap = []
kq = 0

for i in range(n):
    x = a[i] - i

    heapq.heappush(heap, -x)

    Max = -heap[0]

    if Max > x:
        kq += Max - x

        heapq.heappop(heap)
        heapq.heappush(heap, -x)

print(kq)