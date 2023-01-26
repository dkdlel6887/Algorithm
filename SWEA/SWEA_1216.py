def dfs(i, j, N):   # 도착가능 여부 판단
    global yespath
      # 방문기록 위한 N*N행렬
    if maze[i][j] == 3:
        yespath = 1
        return
    for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:   # 우, 하, 좌, 상 순으로 탐색
        ni = i+di
        nj = j+dj
        if maze[ni][nj] != 1 and visited[ni][nj] == 0:
        # ni,nj가 미로 범위 내에 존재 + 벽이 아님 + 방문한 적 없음
            visited[ni][nj] = 1
            dfs(ni,nj,N)
    return

N = 16

for _ in range(1,11):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    yespath = 0
    sti, stj = -1, -1    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sti, stj = i, j
                break
        if sti != -1:
            break
    dfs(sti,stj, N)
    print(f'#{tc} {yespath}')