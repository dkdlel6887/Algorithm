# Tomato
# 상자 안 토마토가 상하좌우에 위치한 토마토에 영향미침 / 대각선 영향 X
# input    1:익은 토마토, 0:안익은 토마토, -1: 빈칸
# output   0: 처음부터 모두익은 상태, -1: 모두 익지 못하는 상태, n: 모두 익는데 걸리는 시간

# 유사문제: 시작점 여러개인 미로, 사방으로 동시에 이동할 경우 빈칸이 없어지는데 걸리는 시간(1초에 한칸이동)
from collections import deque    # 제일 중요!!! 이거 안쓰면 시간초과

def bfs(M,N):
    days = 0  # 익는데 걸리는 일수
    visited = [[0]*M for _ in range(N)]
    q = deque([])    # 원래는 q = []
    for i in tomato:
        q.append(i)       # 시작점 모두 삽입
    for i,j in q:
        visited[i][j] = 1    # 방문 처리
    while q:
        i,j = q.popleft()   # 큐에서 첫번째거 내보내버리기   q.pop(0) 쓰면 timeover
        for di, dj in [[1,0],[0,1],[-1,0],[0,-1]]:
            ni, nj = i + di, j+dj
            if 0<=ni<N and 0<=nj<M and visited[ni][nj]==0 and box[ni][nj] != -1:
                visited[ni][nj] = visited[i][j] + 1   # 시간에 따라 1씩 추가 + 방문처리
                q.append((ni,nj))  # 큐에 새로 추가
    for x in range(N):
        for y in range(M):
            if visited[x][y] == 0 and box[x][y] != -1:    # 빈박스가 아닌데 익을 수 없는 상태가 있는 경우
                return -1
            if days <= visited[x][y]:
                days = visited[x][y]
    return days-1

M, N = map(int,input().split())
box = [list(map(int,input().split())) for _ in range(N)]
tomato = []
cnt = 0  # 안익은 과일 수
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            tomato.append((i,j))   # 시작점이 되는 토마토 좌표 저장
        if box[i][j] == 0:  # 안익은 과일 개수 파악
            cnt += 1
if cnt == 0:  # 처음부터 모두 익은 상태일때
    ans = 0
else:
    ans = bfs(M,N)
print(ans)