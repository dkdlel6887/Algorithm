# 근손실
from itertools import *

W = 500
N, K = map(int,input().split())
kit = list(permutations((map(int,input().split())),N))

#N! 개의 경우의 수에서 항상 W>=500인 경우의 수
ans = 0
for i in range(len(kit)):
    kit[i] = list(kit[i])
    checknum = 0
    for j in range(N):
        n = kit[i][j]
        W = W-K+n
        if W >= 500:
            checknum += 1
        else:
            break
    W = 500
    if checknum == N:
        ans += 1
print(ans)