# string, join 사용하는게 시간 적게 소요
from collections import deque, defaultdict, Counter
import sys
n = int(sys.stdin.readline())
answer = ['-1']*n
a = list(sys.stdin.readline().split())
stack = deque([(a[0],0)])
a_Counter = Counter(a)
for j in range(1,n):
    while stack and a_Counter[stack[-1][0]] < a_Counter[a[j]]:
        val, idx = stack.pop()
        answer[idx] = a[j]
    stack.append((a[j],j))
print(" ".join(answer))
'''
from collections import deque, defaultdict, Counter
import sys
n = int(sys.stdin.readline())
answer = [-1]*n
a = list(sys.stdin.readline().split())
stack = deque([(a[0],0)])
a_Counter = Counter(a)
for j in range(1,n):
    while stack and a_Counter[stack[-1][0]] < a_Counter[a[j]]:
        val, idx = stack.pop()
        answer[idx] = a[j]
    stack.append((a[j],j))
print(*answer)
'''

