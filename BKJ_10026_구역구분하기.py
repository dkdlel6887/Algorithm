import sys
sys.setrecursionlimit(1000000)  # 없으면 runtime error
input = sys.stdin.readline
N = int(input())
arr = list(list(input()) for _ in range(N))

result, result2 = 0, 0
di = [0, 1, 0, -1]  # 우 하 좌 상
dj = [1, 0, -1, 0]

def rgb_Find(i,j):
    color = arr[i][j]
    if visited[i][j] != -1 and arr[i][j] == color:
        visited[i][j] = -1
        for k in range(4):
            ni = i+di[k]
            nj = j+dj[k]
            if 0<=ni<N and 0<=nj<N and visited[ni][nj] != -1 and arr[ni][nj] == color:
                rgb_Find(ni,nj)
#정상
visited = list([0]*N for _ in range(N))
for i in range(N):
    for j in range(N):
        if visited[i][j]==0:
            rgb_Find(i,j)
            result += 1

#색약
for a in range(N):
    for b in range(N):
        if arr[a][b] == 'G':
            arr[a][b] = 'R'
visited = list([0] * N for _ in range(N))
for i in range(N):
    for j in range(N):
        if visited[i][j]==0:
            rgb_Find(i,j)
            result2 += 1

print(f'{result} {result2}')