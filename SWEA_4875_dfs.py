# 4875번 문제 dfs를 사용하여 푼 코드
def dfs(r, c):
    visited[r][c] = True # 이동경로 기록
    if data[r][c] == 3:  # 현좌표 확인
        return 1

    # 순서: 우 하 좌 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    for d in range(4):
        new_r = dr[d] + r  # r:4 + 0
        new_c = dc[d] + c  # c:3 + 1
        if N > new_r >= 0 and N > new_c >= 0 and data[new_r][new_c] != 1 and not visited[new_r][new_c]:
            if dfs(new_r, new_c) == 1:
                return 1
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    visited = [[False] * N for _ in range(N)]
    data = [list(map(int, input().strip())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if data[i][j] == 2:
                r = i
                c = j
    ans = dfs(r, c)
    if ans != 1 and ans != 0:
        ans = 'error'
    print(f'{tc} {ans}')