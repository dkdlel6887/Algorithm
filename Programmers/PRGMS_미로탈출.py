from collections import deque
def solution(maps):
    answer = -1
    ans = 0
    h = len(maps)
    w = len(maps[0])
    visited = [[0]*w for _ in range(h)]
    '''
    1. S 위치 찾기
    2. BFS로 S->L 최단거리 구하기
    3. BFS로 L->E 최단거리 구하기
    '''
    q = deque([])
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 'S':
                q.append((i,j))
    
    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    while q:
        i, j = q.popleft()
        for di,dj in directions:
            ni = i+di
            nj = j+dj
            if 0<=ni<h and 0<=nj<w and maps[ni][nj]!='X' and visited[ni][nj]==0:
                if maps[ni][nj] == 'L':
                    ans = visited[i][j]+1
                    visited = [[0]*w for _ in range(h)]
                    visited[ni][nj]=1
                    q = deque([(ni,nj)])
                    break
                elif ans != 0 and maps[ni][nj]=='E':
                    answer = ans + visited[i][j]
                    return answer
                else:
                    visited[ni][nj] = visited[i][j]+1
                    q.append((ni,nj))
    return answer