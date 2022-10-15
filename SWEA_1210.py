# 1210. [S/W 문제해결 기본] 2일차 - Ladder1
"""
100 X 100 2차원배열
모두 0인 상태
갈 수 있는 길은 1
지나간 길은 0으로 변경
최종 도착점은 2

> 출발점을 알아내는게 목표
2에서 출발
좌우 살피고 1이면 이동
좌우 1없을 시 위로 이동
y축 = 0 이면 위치 반환하고 종료
"""
"""
def lr_check(x):
    for i in range(len(x)):
        for j in range(len(x[i])):
            loc = x[i][j]
            if x[i][j+1] == 1:
                x[i][j] = 0
                loc = x[i][j+1]
            elif x[i][j-1] == 1:
                x[i][j] = 0
                loc = x[i][j-1]
"""
"""
def sadari_find_start(sadari):
    i = len(sadari)
    j = len(sadari[i])
    final = sadari[i][sadari[j].index(2)]

    i = i-1
    final_a = sadari[i-1][sadari[j].index(2)] # 도착점 바로 위칸

    visited = []

    if sadari[98][sadari[99].index(2)+1] == 1:
        location = sadari[98][sadari[99].index(2)+1]
    elif sadari[98][sadari[99].index(2)-1] == 1:
        location = sadari[98][sadari[99].index(2)-1]
    else:
        location = sadari[97][sadari[99].index(2)]
"""


def sadari(data, i, x):
    global ans
    if x < 99 and data[i][x + 1] == 1:  # 오른쪽 확인
        data[i][x] = 0   # 지나간 길 0으로 변경
        x = x + 1
    elif x > 0 and data[i][x - 1] == 1:  # 왼쪽 확인
        data[i][x] = 0
        x = x - 1
    elif i > 0:   # 좌우 확인 후 위칸으로 이동
        i = i-1
    else:         # y좌표가 0인 경우
        ans = x     # 출발지 x좌표 저장
        return
    sadari(data, i, x)


T = 10
for _ in range(1, T+1):
    ans = 0
    tc = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]

    i = len(data)-1
    x = data[len(data)-1].index(2)
    a = sadari(data, i, x)
    print(f'#{tc} {ans}')