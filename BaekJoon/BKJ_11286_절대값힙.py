import sys
from collections import deque
from queue import PriorityQueue
from heapq import heapify

n = int(sys.stdin.readline())
xlst = list(int(sys.stdin.readline()) for _ in range(n))
que = PriorityQueue()
cnt = 0
for i in xlst:
    if i != 0:
        que.put((abs(i),i))
        cnt+=1
    else:
        if cnt>0:
            print(que.get()[1])
            cnt-=1
        else:
            print(0)
'''
# 다른사람 풀이, heap사용, 시간공간 복잡도 less
import sys
input = sys.stdin.readline

import heapq
n = int(input())
heapdata = []
for i in range(n):
    num = int(input())
    if num != 0 :
        heapq.heappush(heapdata,(abs(num),num))
    else:
        if heapdata:
            print(heapq.heappop(heapdata)[1])
        else:
            print(0)
'''
