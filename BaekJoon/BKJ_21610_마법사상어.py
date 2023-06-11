# nxn maps
# 각 좌표마다 물량 표시
# maps 범위 벗어나는 경우 -> 0보다 작으면 n열
# m 명령개수, 1부터 순서대로 ←, ↖, ↑, ↗, →, ↘, ↓, ↙ (좌, 좌상, 상, 우상, 우, 우하, 하, 좌하)
# d, s (m개)
# 비바라기 (n, 1), (n, 2), (n-1, 1), (n-1, 2)

from collections import deque
import sys

# 구름 이동량 결정


# 방향대로 모든 구름 좌표 변경
def mv_cloud(clouds, order, n):  # clouds -> [[n, 1], [n, 2], [n-1, 1], [n-1, 2]] 이중리스트 형태
    directions = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]

    for i in range(len(clouds)):
        y, x = clouds.popleft()
        y = (y + directions[order[0] - 1][0] * order[1]) % n
        x = (x + directions[order[0] - 1][1] * order[1]) % n
        y = y if y >= 0 else y + n
        x = x if x >= 0 else x + n
        maps[y][x] += 1
        visited[y][x] = 1
        clouds.append([y, x])

        # y = (clouds[i][0] + directions[order[0] - 1][0] * order[1]) % n
        # x = (clouds[i][1] + directions[order[0] - 1][1] * order[1]) % n
        # clouds[i][0] = y if y >= 0 else y + n
        # clouds[i][1] = x if x >= 0 else x + n
        # maps[clouds[i][0]][clouds[i][1]] += 1  # 구름있는 칸 물 +1

    return clouds


def cloud_around(clouds):
    n = len(maps)
    directions = [[-1, -1], [-1, 1], [1, -1], [1, 1]]  # 대각선 체크
    for cloud in clouds:
        cnt = 0
        for direction in directions:
            y = cloud[0] + direction[0]
            x = cloud[1] + direction[1]
            if 0 <= y < n and 0 <= x < n and maps[y][x] > 0:
                cnt += 1
        maps[cloud[0]][cloud[1]] += cnt
    return clouds


def find_cloud(clouds):  # 이중포문+in+maps변경
    # n_clouds = deque()
    l = len(clouds)
    for i in range(len(maps)):
        for j in range(len(maps)):
            # if [i,j] not in clouds and maps[i][j] >= 2:  #시간초과 주범
            if visited[i][j] == 0 and maps[i][j] >= 2:
                # n_clouds.append([i, j])
                clouds.append([i, j])
                maps[i][j] -= 2
    for _ in range(l):
        clouds.popleft()
    return clouds


def main():
    global maps, visited
    input = sys.stdin.readline
    n, m = map(int, input().split())
    maps = list(list(map(int, input().split())) for _ in range(n))
    orders = list(list(map(int, input().split())) for _ in range(m))
    clouds = deque([[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]])
    for order in orders:
        visited = [[0] * n for _ in range(n)]
        clouds = find_cloud(cloud_around(mv_cloud(clouds, order, n)))
    water = sum(sum(maps[i]) for i in range(n))
    print(water)


if __name__ == "__main__":
    main()
