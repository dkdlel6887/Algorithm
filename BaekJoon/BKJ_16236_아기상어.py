# 물고기 크기 - 같으면 통과 가능 - 크면 아무것도 못함 - 작으면 먹거나 통과 가능
# 거리 가까운 물고기 먼저, 가장 위에 있는 물고기 먼저, 가장 왼쪽에 있는 물고기 먼저
# 상어 크기(기본 2) 물고기 개수를 자신 크기 만큼 먹을 때 +1
# 상어가 몇초간 살아있는지 -> 물고기 먹을거 없을때 까지 이동한 거리 == 시간
import math
from collections import deque

# [먹을수 있는 물고기 목록 탐색 -> 상어-물고기 간 이동가능여부 및 거리 계산 -> 거리, 행, 열 순으로 정렬]
# -> 상어 좌표 변경, 물고기 좌표 0으로 변경 -> 상어, 먹은 물고기 총량 크기 비교 후 상어 사이즈 변경

# 전체 반복


def find_fish(maps):
    fish_info = []  # 먹을수 있는 물고기 목록 탐색
    for i in range(n):
        for j in range(n):
            if maps[i][j] != 0 and maps[i][j] != 9 and maps[i][j] < ssize:  # 물고기가 있고 자신보다 작은 사이즈이면
                fish_info.append([i, j, maps[i][j]])
    return fish_info


def ch_edible(fish_info, ssize):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for i in range(len(fish_info)):  # 물고기 좌표 별 방문 가능한지 체크 + 거리계산
        visited = [[0] * n for _ in range(n)]
        visited[shark[0]][shark[1]] = -1
        q = deque([shark])
        gotfish = 0
        while q:
            y, x = q.popleft()
            if y == fish_info[i][0] and x == fish_info[i][1]:  # 물고기 좌표와 일치하는 경우 break
                fish_info[i].append(visited[y][x])  # 물고기 좌표, 물고기 크기, 거리 append
                gotfish += 1
                break
            for dy, dx in directions:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < n and 0 <= nx < n and maps[ny][nx] <= ssize and visited[ny][nx] == 0:
                    if visited[y][x] == -1:
                        visited[ny][nx] = 1
                    else:
                        visited[ny][nx] = visited[y][x] + 1  # 방문처리+거리계산
                    q.append([ny, nx])
        if gotfish == 0:
            fish_info[i].append(99)  # 못가는 위치는 거리 100으로 입력
    return fish_info


def sort_fish(fish_info):
    sorted_fish = sorted(fish_info, key=lambda x: (x[3], x[0], x[1]))
    if len(sorted_fish) > 0:
        return sorted_fish[0]  # 첫번째 물고기만 반환
    else:
        return [0, 0, 0, 99]


if __name__ == "__main__":
    n = int(input())
    maps = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if maps[i][j] == 9:
                shark = [i, j]
    maps[shark[0]][shark[1]] = 0
    ssize = 2  # 상어 사이즈
    fsize = 0  # 물고기 먹은 양
    time = 0

    while True:
        fish_info = ch_edible(find_fish(maps), ssize)
        sorted_fish = sort_fish(fish_info)

        if sorted_fish[3] == 99:
            break

        shark = [sorted_fish[0], sorted_fish[1]]  # 물고기 위치로 이동
        fsize += 1  # sorted_fish[2]  # 물고기 먹은 마리수 추가
        maps[sorted_fish[0]][sorted_fish[1]] = 0  # 물고기 제거

        if fsize == ssize:
            ssize += 1
            fsize = 0

        time += sorted_fish[3]  # 시간 추가

    print(time)
