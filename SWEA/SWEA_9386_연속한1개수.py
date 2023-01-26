# 1<=T<=10, 10<=N<=1000
# 연속한 1의 개수 중 최대값
tc = int(input())
for n in range(tc):
    N = int(input())
    lst = list(map(int, input().strip()))
    one = 0
    maxV = 0
    for i in range(N):
        if lst[i] == 1:
            one += 1  # 1이 있을 경우 증가
        else:
            if maxV < one:
                maxV = one
            one = 0
        if i == N-1 and maxV < one:
            maxV = one
    print(f'#{n+1} {maxV}')

    '''
    # 연속한 1의 개수 중 최대값
tc = int(input())
for n in range(tc):
    N = int(input())
    lst = list(map(int, input().strip()))
    one = 0
    for i in range(N):
        if lst[i] == 1:
            one += 1  # 1이 있을 경우 증가
            lst[i] = one
        else:
            one = 0
    print(f'#{n+1} {max(lst)}')'''