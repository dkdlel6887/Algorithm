# 벽은 총 3개 설치가능
# 바이러스는 3개 설치후 열린공간은 한번에 다퍼짐
# 바이러스 >= 2개, <= 10개, 빈칸은 3개 이상
# 1) 2가 퍼지는 함수를 구현(dfs or bfs)
# 2) 1이 3군데 위치하는 조합 모두 구한다
# 3) 각 조합마다 2가 퍼진 뒤 0의 개수를 구해서 최대값을 찾는다.

from collections import deque
from itertools import combinations
import copy

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

q = deque([])
spaces = []
for i in range(n):
    for j in range(m):
        if lab[i][j] == 2:
            q.append((i, j))  # y,x
        if lab[i][j] == 0:
            spaces.append((i, j))


def bfs(maps, queue):
    direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]  # 하, 좌, 상, 우
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + direction[i][0]
            nx = x + direction[i][1]
            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] == 0:
                maps[ny][nx] = 2
                queue.append((ny, nx))
    zeros = 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                zeros += 1
    return zeros


space_comb = list(combinations(spaces, 3))

answer = 0
for space in space_comb:
    maps = copy.deepcopy(lab)
    queue = copy.deepcopy(q)
    for j in range(3):
        maps[space[j][0]][space[j][1]] = 1
    answer = max(bfs(maps, queue), answer)
print(answer)
