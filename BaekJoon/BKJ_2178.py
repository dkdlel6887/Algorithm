'''
input
4 6
101111
101010
101011
111011

output 13
'''
# bfs 이용하여 최단거리 구하기
def bfs(N,M):
    visited = [[0]*M for _ in range(N)]
    q = []
    q.append((0,0))   # 시작점(0,0) 고정
    visited[0][0] = 1    # 이동 횟수에 첫번째칸 포함

    while q:
        i, j = q.pop(0)  # i, j에 현좌표 저장
        if i == N-1 and j == M-1:   # 현위치가 도착지인 경우 이동횟수 반환
            return visited[i][j]
        for di, dj in [[0,1],[1,0],[-1,0],[0,-1]]:    # 상하좌우 확인
            ni, nj = i+di, j+dj
            if 0<= ni <N and 0<= nj<M and maze[ni][nj] != 0 and visited[ni][nj] == 0:
                q.append((ni,nj))   # 큐에 삽입
                visited[ni][nj] = visited[i][j]+1  # 이동횟수 기록 = 방문기록


N, M = map(int, input().split())
maze = [list(map(int,input().strip())) for _ in range(N)]

print(bfs(N,M))

