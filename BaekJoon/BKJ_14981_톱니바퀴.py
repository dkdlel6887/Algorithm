import sys
from collections import deque

arr = list(deque(map(int, sys.stdin.readline().strip())) for _ in range(4))
r = int(sys.stdin.readline())
rlst = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]

print(arr)
# print(r)
print(rlst)
# 1,3번 -> index 2 / 2,4번 -> index 7
# .rotate(1) -> 시계 , .rotate(-1) -> 반시계
for i in range(r):
    check = [0] * 3  # 극 일치여부 확인
    if arr[0][2] != arr[1][6]:
        check[0] = 1
    if arr[1][2] != arr[2][6]:
        check[1] = 1
    if arr[2][2] != arr[3][6]:
        check[2] = 1
    print(check)
    gear = rlst[i][0] - 1  # 회전시킬 톱니 번호
    arr[gear].rotate(rlst[i][1])  # 톱니 회전

    if gear == 0 and check[0] == 1:
        arr[1].rotate(-1 * rlst[i][1])
        if check[1] == 1:
            arr[2].rotate(rlst[i][1])
            if check[2] == 1:
                arr[3].rotate(-1 * rlst[i][1])
    if gear == 1:
        if check[0] == 1:
            arr[0].rotate(-1 * rlst[i][1])
        if check[1] == 1:
            arr[2].rotate(-1 * rlst[i][1])
            if check[2] == 1:
                arr[3].rotate(rlst[i][1])
    if gear == 2:
        if check[1] == 1:
            arr[1].rotate(-1 * rlst[i][1])
            if check[0] == 1:
                arr[0].rotate(rlst[i][1])
        if check[2] == 1:
            arr[3].rotate(-1 * rlst[i][1])
    if gear == 3 and check[2] == 1:
        arr[2].rotate(-1 * rlst[i][1])
        if check[1] == 1:
            arr[1].rotate(rlst[i][1])
            if check[0] == 1:
                arr[0].rotate(-1 * rlst[i][1])
answer = 0
if arr[0][0] == 1:
    answer += 1
if arr[1][0] == 1:
    answer += 2
if arr[2][0] == 1:
    answer += 4
if arr[3][0] == 1:
    answer += 8

print(arr)
print(answer)
