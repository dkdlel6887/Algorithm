def find_dust(maps, R, C):  # 먼지위치 리스트에 저ㅇ
    dust_lst = []
    for i in range(R):
        for j in range(C):
            if maps[i][j] > 0:
                dust_lst.append([i, j])
    return dust_lst


def dust_diff(maps, R, C, dust_lst):
    dustmaps = [[0] * C for _ in range(R)]
    directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]  # 하 좌 상 우

    for dust in dust_lst:
        y, x = dust[0], dust[1]
        dust_part = maps[y][x] // 5  # 확산
        if dust_part < 1:
            continue
        cnt = 0
        for d in directions:
            ny = y + d[0]
            nx = x + d[1]
            if 0 <= ny < R and 0 <= nx < C and maps[ny][nx] != -1:
                cnt += 1
                dustmaps[ny][nx] += dust_part
        dustmaps[y][x] -= dust_part * cnt
    for i in range(R):
        for j in range(C):
            dustmaps[i][j] += maps[i][j]  # 새로운 먼지지도에 기존 먼지지도 더해줌
    return dustmaps


def clean_air(k, maps):  # k: 미세먼지 좌표 [(k,0),(k+1,0)]
    # direction = [[0, 1], [-1, 0], [0, -1], [1, 0]]  # 반시계방향
    # direction2 = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 시계방향

    # 반시계
    for i in range(k - 1, 0, -1):
        maps[i][0] = maps[i - 1][0]
    for i in range(0, C - 1):
        maps[0][i] = maps[0][i + 1]
    for i in range(0, k):
        maps[i][C - 1] = maps[i + 1][C - 1]
    for i in range(C - 1, 1, -1):
        maps[k][i] = maps[k][i - 1]
    maps[k][1] = 0

    # 시계
    for i in range(k + 2, R - 1):
        maps[i][0] = maps[i + 1][0]
    for i in range(0, C - 1):
        maps[R - 1][i] = maps[R - 1][i + 1]
    for i in range(R - 1, k + 1, -1):
        maps[i][C - 1] = maps[i - 1][C - 1]
    for i in range(C - 1, 1, -1):
        maps[k + 1][i] = maps[k + 1][i - 1]
    maps[k + 1][1] = 0

    return maps


"""
def rotation():
    def top_rotate(): # 위쪽 회전
        d = 1 # 오른쪽 방향으로 시작
        before = 0
        x, y = robot_top, 1 # 공기청정기 머리부분의 바로 오른쪽 칸부터 시작
        while True:
            ax = x + dx[d]
            ay = y + dy[d]
            if ax == R or ay == C or ax == -1 or ay == -1: # 현재 좌표가 꼭짓점인 경우
                d = (d-1)%4
                continue
            if x == robot_top and y == 0: # 한 바퀴 회전 완료해서 공기청정기 좌표로 다시 돌아온 경우
                break
            board[x][y], before  = before, board[x][y]
            x, y = ax, ay

    def bottom_rotate():  # 아래 회전
        d = 1 # 오른쪽 방향으로 시작
        before = 0
        x, y = robot_bottom, 1 # 공기청정기 아래부분의 바로 오른쪽 칸부터 시작
        while True:
            ax = x + dx[d]
            ay = y + dy[d]
            if ax == R or ay == C or ax == -1 or ay == -1: # 현재 좌표가 꼭짓점인 경우
                d = (d+1)%4
                continue
            if x == robot_bottom and y == 0: # 한 바퀴 회전 완료해서 공기청정기 좌표로 다시 돌아온 경우
                break
            board[x][y], before  = before, board[x][y]
            x, y = ax, ay
            
    top_rotate()
    bottom_rotate()
"""


def main():
    global maps, R, C
    R, C, T = map(int, input().split())
    maps = list(list(map(int, input().split())) for _ in range(R))

    k = 0
    for i in range(2, R):
        if maps[i][0] == -1:
            k = i
            break

    for _ in range(T):
        new_maps = dust_diff(maps, R, C, find_dust(maps, R, C))
        maps = clean_air(k, new_maps)

    answer = 2
    for r in range(R):
        answer += sum(maps[r])

    print(answer)


if __name__ == "__main__":
    main()
