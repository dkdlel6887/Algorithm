from collections import deque
def solution(maps):
    answer = []
    n = len(maps)
    m = len(maps[0])
    visited = [[-1]*m for _ in range(n)]
    stack = deque([])
    
    # DFS이용
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]   # 하 우 상 좌

    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and visited[i][j]==-1:  # 시작 
                stack.append((i,j))
                visited[i][j] = 0
                food = 0
                
                while stack:
                    y, x = stack.pop()
                    food += int(maps[y][x])
                    
                    for d in range(4):
                        ny = y+dy[d]
                        nx = x+dx[d]
                        if 0<=ny<n and 0<=nx<m and visited[ny][nx] == -1 and maps[ny][nx] != 'X':
                            visited[ny][nx] = 0
                            stack.append((ny,nx))
                answer.append(food)
    if answer:
        return sorted(answer)
    return [-1]