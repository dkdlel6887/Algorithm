def solution(maps):
    global answer
    N = len(maps)
    M = len(maps[0])
    visited = [[0]*M for _ in range(N)]
    answer = N*M

    def dfs(i,j,maps,s):  # 현위치 i,j, 지도maps, 이동거리s
        global answer
        if i == N-1 and j == M-1 and maps[i][j] == 1:
            if answer > s:  # 최단거리인지 확인
                answer = s
                return
        else:
            di = [0, 1, -1, 0]  # 우, 하, 좌, 상
            dj = [1, 0, 0, -1]
            visited[i][j] = 1  # 방문처리
            for d in range(4):
                ni = i+di[d]
                nj = j+dj[d]
                if 0<=ni<N and 0<=nj<M and visited[ni][nj]==0 and maps[ni][nj] == 1:
                    dfs(ni, nj,maps,s+1)
                    visited[ni][nj] = 0

    # 0,0 시작
    i, j = 0, 0
    s = 1  # 거리
    dfs(i,j,maps,s)
    if answer == N*M:
        answer =  -1
    return answer
maps = [[1,1,0,0,1],
        [0,1,1,1,1],
        [0,1,0,0,1],
        [0,1,1,1,1],
        [0,1,0,0,1]]

print(solution(maps))