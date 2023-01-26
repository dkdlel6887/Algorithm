root = 1

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N-1)]

p = [0]*(N-1)
for i in range(N-1):
    for j in arr:
        if j[i][0] == i+1 or j[i][1] == i+1:
            p[i] = i+1
for i in p:
    print(i)