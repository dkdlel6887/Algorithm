# 20055 포기
'''
2N개의 상자
K: 내구도 0인 칸 최대 개수
'''
from collections import deque
N, K = map(int, input().split())
A = list(map(int,input().split()))  # 내구도 2N개
A = deque(A)
R = deque()
cnt = 0
# 1번 통해서만 로봇 올리기 가능, 1번 내구도 0이되면 로봇 추가 불가
while A.count(0) < K:
    if A[0]>0 and R[0]==0:
        A[0] -= 1
        R[0] += 1  # 로봇 올리기 ~
    A.rotate(1)  # 한칸씩 회전
    R.rotate(1)
    cnt += 1