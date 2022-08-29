# me
N, L = map(int, input().split())
leaks = list(map(int, input().split()))
new_tape = True
tape_start = 0
tape_count = 0

for leak in sorted(leaks):
    if new_tape:
        tape_count += 1
        tape_start = leak
        new_tape = False
        continue
    if leak <= (tape_start + (L - 1)):
        continue
    else:
        tape_count += 1
        tape_start = leak

print(tape_count)

# teacher
N, L = map(int, input().split())
coord = [False] * 1001  # index 1000
for i in map(int, input().split()):
    coord[i] = True

ans = 0
x = 0
while x < 1001:
    if coord[x]:
        ans += 1
        x += L
    else:
        x += 1

print(ans)
