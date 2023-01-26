'''
NxN 정사각형 모양의 미로
출발지에서 목적지 도착하는 경로 유무 확인
결과값 -> 가능: 1, 불가능: 0

통로: 0, 벽:1, 출발:2, 도착:3
N: 5~100, T: 1~50
'''

# BFS 사용해보기
'''   
input
00003
01111
21000
01110
00000
'''
'''
def bfs(i, j, N):
    visited = [[0]*N for _ in range(N)]
    q = []
    q.append((i,j))  # 튜플 삽입
    visited[i][j] = 1
    while len(q)>0:
        i, j = q.pop(0)
        if maze[i][j] == 3:  # 3번 도착지인가?
            return 1
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj]!=1 and visited[ni][nj]==0:
                q.append((ni,nj))
                visited[ni][nj] = visited[i][j]+1
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sti, stj = i, j  # start i,j 저장
                break
        if sti != -1:
            break
'''
# 경로 확인
def bfs(i, j, N):
    visited = [[0] * N for _ in range(N)]  # 방문처리+이동횟수 표시
    q = []
    q.append((i, j))  # 시작위치 삽입
    visited[i][j] = 1

    while len(q) > 0:
        i, j = q.pop(0)  # 큐에서 첫번째 위치 제거 + i, j에 저장
        if maze[i][j] == 3:
            return 1
        for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:  # 미로범위 내+이동가능숫자+미방문
                q.append((ni, nj))  # 현위치 삽입
                visited[ni][nj] = visited[i][j] + 1  # 방문처리+이동한 횟수
        # for 문 반복하면서 4방향 중 방문가능 경로 큐에 삽입
    return 0

# 거리 구하기
def bfs_find_short(i, j, N):
    visited = [[0] * N for _ in range(N)]  # 방문처리+이동횟수 표시
    q = []
    q.append((i, j))  # 시작위치 삽입
    visited[i][j] = 1   # 거리구할 때 시작위치 포함하면 작성

    while len(q) > 0:
        i, j = q.pop(0)
        if maze[i][j] == 3:
            return visited[i][j]  # 3까지의 최단거리
        for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:  # 미로범위 내+이동가능숫자+미방문
                q.append((ni, nj))  # 현위치 삽입
                visited[ni][nj] = visited[i][j] + 1  # 방문처리+이동한 횟수
                # for 문 반복하면서 4방향 중 방문가능 경로 큐에 삽입
    return 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input().strip())) for _ in range(N)]
    sti, stj = -1, -1
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sti, stj = i, j
                break
        if sti != -1:
            break
    print(f'#{tc} {bfs(sti,stj,N)}')
    print(f'최단거리 {bfs_find_short(sti, stj, N)}')