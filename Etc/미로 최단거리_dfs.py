# 미로문제 DFS
# 모든 경로를 돌아보는 코드 >>> 경로의 수 구하기
# 최단 경로 구하기,

'''
NxN 정사각형 모양의 미로
출발지에서 목적지 도착하는 경로 유무 확인
결과값 -> 가능: 1, 불가능: 0

통로: 0, 벽:1, 출발:2, 도착:3
N: 5~100, T: 1~50

input
11111111
12000011
10111001
10130001
10101101
10101101
10001111
11111111
'''

def dfs(i, j, N):
    global answer
    if maze[i][j] == 3:
        answer += 1
        return
    else:
        visited[i][j] = 1
        for di, dj in [[0,1],[1,0],[-1,0],[0,-1]]:
            ni, nj = i+di, j+dj
            if maze[ni][nj]!=1 and visited[ni][nj] == 0:  # 벽으로 둘러싸인 미로
                dfs(ni, nj, N)
        visited[ni][nj] = 0  # 방문했다가 return하는 곳들은 다시 갈수있게 0으로 변경


T = 1  #int(input())
for tc in range(1, T+1):
    N = int(input())
    visited = [[0]*N for _ in range(N)]
    answer = 0

    maze = [list(map(int,input().strip())) for _ in range(N)]
    sti, stj = -1, -1
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sti, stj = i, j
                break
        if sti != -1:
            break
    print(dfs(sti,stj,N))    # 도착지까지
    print(answer)   # 도착지까지 경로 수


# 디버깅 도중 확인하고 싶은 변수가 있는 경우 우클릭 +new watch -> 변수명 입력
# 디버깅 위해 빨강원 표시한 부분만 확인하려면 좌측바에 |▷ 클릭




# 지나온칸 정보 추가, 이동 거리
def dfs2(i, j, s, N):  # s: 이동거리
    global minV    # minV : 최단경로 거리
    if maze[i][j] == 3:
        if minV > s:    # minV : 최단경로 거리
            minV = s    # 시작 포함,도착 제외: s/ 시작,도착 포함: s+1/ 시작,도착 제외: s-1
        return
    else:
        visited[i][j] = 1
        for di, dj in [[0,1],[1,0],[-1,0],[0,-1]]:
            ni, nj = i+di, j+dj
            if maze[ni][nj]!=1 and visited[ni][nj] == 0:  # 벽으로 둘러싸인 미로
                dfs(ni, nj, s+1, N)   # 변경된 값을 넣어 재귀
        visited[ni][nj] = 0  # 방문했다가 return하는 곳들은 다시 갈수있게 0으로 변경

T = 1  #int(input())
for tc in range(1, T+1):
    N = int(input())
    visited = [[0]*N for _ in range(N)]
    minV = N*N

    maze = [list(map(int,input().strip())) for _ in range(N)]
    sti, stj = -1, -1
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sti, stj = i, j
                break
        if sti != -1:
            break
    print(dfs2(sti,stj, 0, N))    # 도착지까지
    if minV == N*N:  # 도착못한 경우
        minV = -1
    print(minV)   # 도착지까지 경로 수