import sys


def solve() -> None:
	data = sys.stdin.buffer.read().split()
	if not data:
		return
	data[0] = data[0].lstrip(b"\xef\xbb\xbf")

	n = int(data[0])
	m = int(data[1])
	k = int(data[2])

	raw = data[3:]
	if len(raw) == 1 and len(raw[0]) == n and all(ch in b"01" for ch in raw[0]):
		teams = bytearray(ch - 48 for ch in raw[0])
	else:
		teams = bytearray(int(raw[i]) for i in range(n))

	teams1 = 0
	for i, t in enumerate(teams):
		if t:
			teams1 |= 1 << i

	mask_all = (1 << n) - 1
	teams0 = mask_all ^ teams1

	# For s = 0, current player loses immediately, so winner is opposite team.
	row = teams0

	if m > 1:
		in_stack = []
		out_stack = []
		size = 0

		for _ in range(1, m):
			# Push previous row to sliding window.
			if in_stack:
				prev_or, prev_and = in_stack[-1][1], in_stack[-1][2]
				in_stack.append((row, prev_or | row, prev_and & row))
			else:
				in_stack.append((row, row, row))
			size += 1

			# Keep only the latest K rows in the window.
			if size > k:
				if not out_stack:
					while in_stack:
						val = in_stack.pop()[0]
						if out_stack:
							prev_or, prev_and = out_stack[-1][1], out_stack[-1][2]
							out_stack.append((val, prev_or | val, prev_and & val))
						else:
							out_stack.append((val, val, val))
				out_stack.pop()
				size -= 1

			in_or = in_stack[-1][1] if in_stack else 0
			out_or = out_stack[-1][1] if out_stack else 0
			exists1_q = in_or | out_or

			if in_stack and out_stack:
				all1_q = in_stack[-1][2] & out_stack[-1][2]
			elif in_stack:
				all1_q = in_stack[-1][2]
			else:
				all1_q = out_stack[-1][2]

			# Map info of player q = p + 1 back to player p (circular right rotation by 1).
			exists1_p = (exists1_q >> 1) | ((exists1_q & 1) << (n - 1))
			all1_p = (all1_q >> 1) | ((all1_q & 1) << (n - 1))

			# If team[p] == 1: win if any previous state for q is 1.
			# If team[p] == 0: win(1) only when all previous states for q are 1.
			row = (teams1 & exists1_p) | (teams0 & all1_p)

	out = ["1" if (row >> i) & 1 else "0" for i in range(n)]
	sys.stdout.write(" ".join(out))


if __name__ == "__main__":
	solve()
