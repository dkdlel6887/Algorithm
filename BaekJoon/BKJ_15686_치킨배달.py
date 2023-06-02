# nxn, r,c->1 start
# chicken distance-> house<>store
from itertools import combinations
import math

# 0:blank, 1:house, 2:store
# 2*n>= home,2<=n<=50 1<=m<=13
n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
store = []
house = []


def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


for i in range(n):
    for j in range(n):
        if maps[i][j] == 2:
            store.append((i, j))
        if maps[i][j] == 1:
            house.append((i, j))

# store 좌표 전체 combination
storelst = [i for i in combinations(store, m)]
# print(storelst)
answer = 1e9
for stores in storelst:  # ((0, 1), (3, 0)), ((0, 1), (4, 0))
    distan = 0
    for h in house:
        dis = 1e9
        for s in stores:  # ((0, 1), (3, 0))
            dis = min(dis, distance(s, h))
        distan += dis
    answer = min(answer, distan)
print(answer)
# 1. 집 하나당 가게별 거리 계산 후 가장 작은 값 찾기
# 2. 모든 집 별 가장 짧은 거리로 모두 더해 총 거리 계산
# 3. 모든 가게위치 경우의 수 별 거리 계산값 중 가장 작은 값 return
