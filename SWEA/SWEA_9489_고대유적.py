def findmax(N,M,arr):
    maxV=0
    # 행에서 최대연속값 찾기
    for i in range(N):
        cnt = 0
        for j in range(M):
            if arr[i][j] == 1:
                cnt+=1
                if maxV < cnt:
                    maxV = cnt
            else:
                cnt = 0
    # 열에서 최대연속값 찾기
    for i in range(M):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 1:
                cnt+=1
                if maxV < cnt:
                    maxV = cnt
            else:
                cnt = 0
    return maxV

tc = int(input())
for n in range(1, tc+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    print(f'#{n} {findmax(N,M,arr)}')

'''
만약 N, M이 서로 같은 값이면 for 문을 따로 만들 필요 없이 
arr[i][j], arr[j][i]로 입력하면 된다.'''