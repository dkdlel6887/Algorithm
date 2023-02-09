import sys
N, M = map(int, sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))

# N = len(A), M = A[i] ~ A[j] sum
answer = 0
s = 0
e = 0
sumi=0
while s<N:
    if e<N:
        sumi+=A[e]
        if sumi<M:
            e+=1
        elif sumi==M:
            answer+=1
            s+=1
            e=s
            sumi=0
        else:
            s+=1
            e=s
            sumi=0
    else:  # 끝까지 더해도 M보다 작은 경우엔 그 뒤는 할 필요가 없으므로 break
        break
print(answer)