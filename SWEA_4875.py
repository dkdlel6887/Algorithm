'''
NxN 정사각형 모양의 미로
출발지에서 목적지 도착하는 경로 유무 확인
결과값 -> 가능: 1, 불가능: 0

통로: 0, 벽:1, 출발:2, 도착:3
N: 5~100, T: 1~50
'''

# DFS 사용해보기
'''   input
00003
01111
21000
01110
00000
'''
# 2번째 pass 답안 (간결하게 만듬)
def find_way(miro, x, y, N):
    if miro[y][x] == 3:
        return 1
    else:
        if x > 0 and (miro[y][x - 1] == 0 or miro[y][x - 1] == 3):  # 좌측 확인
            miro[y][x] = -1  # 지나온 길 표시
            if find_way(miro, x-1, y, N) == 1: return 1
        if y < N-1 and (miro[y + 1][x] == 0 or miro[y + 1][x] == 3):  # 하
            miro[y][x] = -1
            if find_way(miro, x, y+1, N) == 1: return 1
        if x < N-1 and (miro[y][x + 1] == 0 or miro[y][x + 1] == 3):  # 우
            miro[y][x] = -1
            if find_way(miro, x+1, y, N) == 1: return 1
        if y > 0 and (miro[y - 1][x] == 0 or miro[y - 1][x] == 3):  # 상
            miro[y][x] = -1
            if find_way(miro, x, y-1, N) == 1: return 1
        return 0  # 길 없는 경우

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    miro = [list(map(int, input().strip())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                y = i
                x = j
    ans = find_way(miro, x, y, N)
    if ans != 1 and ans != 0:
        ans = 'error'
    print(f'#{tc} {ans}')

'''  첫 pass 답안, 도착점에서 출발점으로 이동
def find_way(miro, N):
    global ans, x, y
    if miro[y][x] == 2:
        ans = 1
        return
    else:
        if x > 0 and (miro[y][x - 1] == 0 or miro[y][x - 1] == 2):  # 좌측 확인
            miro[y][x] = -1  # 지나온 길 표시
            x = x-1
            find_way(miro, N)
            x = x+1
            if ans == 1: return
        if y < N-1 and (miro[y + 1][x] == 0 or miro[y + 1][x] == 2):  # 하
            miro[y][x] = -1
            y = y+1
            find_way(miro, N)
            y = y-1
            if ans == 1: return
        if x < N-1 and (miro[y][x + 1] == 0 or miro[y][x + 1] == 2):  # 우
            miro[y][x] = -1
            x = x+1
            find_way(miro, N)
            x = x-1
            if ans == 1: return
        if y > 0 and (miro[y - 1][x] == 0 or miro[y - 1][x] == 2):  # 상
            miro[y][x] = -1
            y = y-1
            find_way(miro, N)
            y = y+1
            if ans == 1: return
        if ans != 1:
            ans = 0
        return  # 길 없는 경우

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    miro = [list(map(int, input().strip())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 3:
                y = i
                x = j
    ans = 'error'
    find_way(miro, N)
    print(f'#{tc} {ans}')
'''
### temp_x, temp_y 는 마지막 2,2 위치에서 return 하게되면 2,3 위치에서 가지고 있던 값을 가지는게 아닌가? 놉 애초에 상하좌우 확인 후 [x = temp_x]를 할 때 temp_x가 초기화되지 않은 상태이기 때문에 오류가 발생함

'''
def find_way(miro, x, y, N):
    global ans
    if miro[y][x] == 3:
        ans = 1
        return
    else:
        if x > 0 and (miro[y][x - 1] == 0 or miro[y][x - 1] == 3):  # 좌측 확인
            miro[y][x] = -1  # 지나온 길 표시
            temp_x, temp_y = x, y
            x = x-1
            find_way(miro, x, y, N)
            if ans == 1: return
        if y < N-1 and (miro[y + 1][x] == 0 or miro[y + 1][x] == 3):  # 하
            miro[y][x] = -1
            temp_x, temp_y = x, y
            y = y+1
            find_way(miro, x, y, N)
            if ans == 1: return
        if x < N-1 and (miro[y][x + 1] == 0 or miro[y][x + 1] == 3):  # 우
            miro[y][x] = -1
            temp_x, temp_y = x, y
            x = x+1
            find_way(miro, x, y, N)
            if ans == 1: return
        if y > 0 and (miro[y - 1][x] == 0 or miro[y - 1][x] == 3):  # 상
            miro[y][x] = -1
            temp_x, temp_y = x, y
            y = y-1
            find_way(miro, x, y, N)
            if ans == 1: return
        if ans != 1:
            ans = 0
            x, y = temp_x, temp_y
        return  # 길 없는 경우

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    miro = [list(map(int, input().strip())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                y = i
                x = j
    ans = 'error'
    find_way(miro, x, y, N)
    print(f'#{tc} {ans}')
'''