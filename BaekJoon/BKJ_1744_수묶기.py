# 60+ min
from collections import deque
N = int(input())
lst = list(int(input()) for _ in range(N))
lst.sort()    # lst = sorted(lst,reverse=True)
minus = deque()
plus = deque()

answer = 0
zcnt = 0
ocnt = 0
# 음수인 경우 음수랑 곱함
# 0인 경우 더하거나 음수랑 곱함
# 양수인 경우 차례로 곱함

for n in range(len(lst)):
    if lst[n] < 0:
        minus.append(lst[n])
    elif lst[n] == 0:
        zcnt += 1
    elif lst[n] == 1:
        ocnt += 1
    else:
        plus.append(lst[n])
m = len(minus)
p = len(plus)

# 1인 경우
answer += ocnt

# 음수
if m != 0 and m % 2 == 0:
    for i in range(0, m - 1, 2):
        answer += minus[i] * minus[i + 1]
elif m != 1 and m != 0:
    for i in range(0, m - 2, 2):
        answer += minus[i] * minus[i + 1]
    if zcnt == 0:  # 0이 없는 경우
        answer += minus[m - 1]
elif m == 1 and zcnt == 0:
    answer += minus[0]
# 양수
if p != 0 and p % 2 == 0:
    for i in range(p - 1, 0, -2):  # 6 -> 531 / 420
        answer += plus[i] * plus[i - 1]
elif p != 1 and p != 0:
    for i in range(p - 1, 0, -2):  # 5-> 42 / 31
        answer += plus[i] * plus[i - 1]
    answer += plus[0]
elif p == 1:
    answer += plus[0]


print(answer)