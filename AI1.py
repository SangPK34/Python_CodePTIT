import sys
from collections import deque


def get_inversions(state):
    inv = 0
    arr = [x for x in state if x != 0]
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inv += 1
    return inv


def solve():
    input_data = []

    for line in sys.stdin:
        input_data.extend(line.split())
        if len(input_data) >= 18:
            break

    if len(input_data) < 18:
        return

    start_state = tuple(map(int, input_data[:9]))
    goal_state = tuple(map(int, input_data[9:18]))

    if start_state == goal_state:
        print(0)
        return

    if get_inversions(start_state) % 2 != get_inversions(goal_state) % 2:
        print("UNSOLVABLE")
        return

    queue = deque([(start_state, 0)])
    visited = set([start_state])

    moves = {
        0: (1, 3), 1: (0, 2, 4), 2: (1, 5),
        3: (0, 4, 6), 4: (1, 3, 5, 7), 5: (2, 4, 8),
        6: (3, 7), 7: (4, 6, 8), 8: (5, 7)
    }

    while queue:
        curr_state, steps = queue.popleft()
        idx = curr_state.index(0)

        for next_idx in moves[idx]:
            new_state = list(curr_state)
            new_state[idx], new_state[next_idx] = new_state[next_idx], new_state[idx]
            new_state_tuple = tuple(new_state)

            if new_state_tuple == goal_state:
                print(steps + 1)
                return

            if new_state_tuple not in visited:
                visited.add(new_state_tuple)
                queue.append((new_state_tuple, steps + 1))


if __name__ == '__main__':
    solve()