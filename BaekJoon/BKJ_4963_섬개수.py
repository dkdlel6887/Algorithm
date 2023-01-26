from sys import stdin
from collections import deque

def find_land(maps,w,h):
    global ans
    for row in range(h):
        for col in range(w):
            if maps[row][col] == 1:
                i, j = row, col
                find_island(maps, i, j)
    return ans

def find_island(maps, i, j):
    global ans
    q = deque()
    di = [1, 1, 0, -1, -1, -1,  0,  1]  # 남, 남서, 서, 북서, 북, 북동, 동, 남동
    dj = [0, 1, 1,  1,  0, -1, -1, -1]
    maps[i][j] = -1
    q.append((i, j))
    while q:
        i, j = q.popleft()
        for n in range(8):
            ni = i+di[n]
            nj = j+dj[n]
            if 0 <= ni < h and 0 <= nj < w and maps[ni][nj] == 1:
                maps[ni][nj] = -1  # 방문 처리
                q.append((ni, nj))  # 큐에 land 좌표 추가
            elif 0 <= ni < h and 0 <= nj < w and maps[ni][nj] != -1:
                maps[ni][nj] = -1  # 방문 처리
    ans += 1

while True:
    w, h = map(int, stdin.readline().split())
    if w == 0 and h == 0:
        break
    elif w > 1 and h > 1:
        maps = [list(map(int, stdin.readline().split())) for _ in range(h)]
    else:
        maps = int(stdin.readline())
        if maps == 1:
            print(1)
            continue
        else:
            print(0)
            continue
    ans = 0
    print(find_land(maps, w, h))