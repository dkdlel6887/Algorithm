from collections import deque

n, m = map(int, input().split())
friend = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)

q = deque()
cnt = 99

for i in range(1, n + 1):
    visited = [-1 for _ in range(n + 1)]
    visited[i] = 0
    q.append(i)
    while q:
        p = q.popleft()
        adj = friend[p]  # 인접 목록
        for j in adj:
            if visited[j] == -1:
                q.append(j)
                visited[j] = visited[p] + 1

    val = min(sum(visited) + 1, cnt)
    if cnt > val:
        cnt = val
        ans = i

print(ans)
