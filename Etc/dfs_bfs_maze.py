# N*N 행렬, 시작점 2, 도착점 3, 벽 1, 길 0

# 1) DFS 사용하여 도착점까지 경로의 수 구하기
def dfs(i, j, N):   # 도착가능 여부 판단
    global yespath

    if maze[i][j] == 3:
        yespath = 1
        return 1  # 도착가능 여부 표시
    for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:   # 우, 하, 좌, 상 순으로 탐색
        ni = i+di
        nj = j+dj
        if 0<=ni<N and 0<=nj<N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
        # ni,nj가 미로 범위 내에 존재 + 벽이 아님 + 방문한 적 없음
            visited[ni][nj] = 1
            dfs(ni,nj,N)
    return 0  # 도착점 못찾은 경우
# 2) DFS 사용하여 최단거리 구하기
def dfs_ans(i, j, N):   # 최단경로
    global ans # 최단 경로
    if maze[i][j] == 3:
        # visited[i][j] =+ 1   # 시작 위치 포함 시
        ans = min(visited[i][j], ans)
        return
    for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:   # 우, 하, 좌, 상 순으로 탐색
        ni = i+di
        nj = j+dj
        if 0<=ni<N and 0<=nj<N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
        # ni,nj가 미로 범위 내에 존재 + 벽이 아님 + 방문한 적 없음
            visited[ni][nj] = visited[i][j]+1   # 거리구할때 용이
            dfs_ans(ni,nj,N)
# 3) DFS 사용하여 도착가능 여부 구하기
def dfs_cnt(i, j, N):  # 경로의 수
    global cnt
    visited[i][j] = 1
    if maze[i][j] == 3:
        cnt += 1   # 도착 경로 발견 시 +1
        return
    for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:   # 우, 하, 좌, 상 순서로 탐색
        ni = i+di
        nj = j+dj
        if 0<=ni<N and 0<=nj<N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
        # ni,nj가 미로 범위 내에 존재 + 벽이 아님 + 방문한 적 없음
            dfs_cnt(ni,nj,N)
            visited[ni][nj] = 0  # 방문 후 되돌아감을 표시, 다른 경로로 방문 가능하도록 함


T = 10  # test case 개수

for _ in range(1,T+1):
    N = int(input())  # N*N행렬
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]  # 방문기록 위한 N*N행렬
    yespath = 0
    ans = N*N   # 행렬의 크기와 비교하여 작은 값을 경로의 길이로 설정
    cnt = 0
    sti, stj = -1, -1    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sti, stj = i, j
                break
        if sti != -1:
            break
    dfs(sti,stj, N)
    #dfs_ans(sti, stj, N)
    #dfs_cnt(sti, stj, N)
    print(f'{yespath} {ans} {cnt}')
"""    
1111111111111111
1200000000100011
1010101110101111
1000100010100011
1111111010101011
1000000010101011
1011111110111011
1010000010001011
1010101111101011
1010100010001011
1010111010111011
1010001000100011
1011101111101011
1000100000001311
1111111111111111
1111111111111111
"""

# 4) BFS 사용하여 도착점까지 경로의 수 구하기
# 5) BFS 사용하여 최단거리 구하기
# 6) BFS 사용하여 도착가능 여부 구하기