# x1,y1,r1 -> 원 1,    x2,y2,r2 -> 원 2, 교점의 개수 구하는 문제

# r1+r2 < 두 점사이의 거리 -> 0개
# |r2 - r1| > 두 점사이의 거리 -> 0개
# r1+r2 == 두 점사이의 거리 -> 1개
# |r2 - r1| == 두 점사이의 거리 -> 1개
# |r2 - r1| < 두 점사이의 거리 < r1+r2 -> 2개
# r1==r2, 두점사이의 거리==0 -> -1(무한대)

"""
3
0 0 13 40 0 37
0 0 3 0 7 4
1 1 1 1 1 5
"""
tc = int(input())
for _ in range(tc):
    xyr = list(map(int,input().split()))
    # xyr = list(map(int,"0 0 13 40 0 37".split()))
    x1 = xyr[0]
    y1 = xyr[1]
    r1 = xyr[2]
    x2 = xyr[3]
    y2 = xyr[4]
    r2 = xyr[5]
    
    rlen = ((x1-x2)**2+(y1-y2)**2)**0.5
    if rlen > r1+r2 or abs(r2-r1) > rlen:
        answer = 0
    if rlen == r1+r2 or rlen == abs(r2-r1):
        answer = 1
    if abs(r2-r1) < rlen < r1+r2:
        answer = 2
    if r1==r2 and rlen == 0:
        answer = -1
    print(answer)