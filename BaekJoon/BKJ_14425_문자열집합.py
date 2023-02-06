import sys
N,M = map(int, input().split())
nset = set(sys.stdin.readline().strip() for _ in range(N))
mlist = list(sys.stdin.readline().strip() for _ in range(M))
cnt = 0
for m in mlist:
    if m in nset:
        cnt += 1
print(cnt)