from collections import deque

def solution(queue1, queue2):
    count = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    s1 = sum(queue1)
    s2 = sum(queue2)
    sumq = (s1+s2)
    sumq2 = sumq//2
    cnt = len(queue1)*3
    if sumq % 2 != 0 or max(queue1) > sumq2 or max(queue2) > sumq2:
        return -1
    while count < cnt:
        if s1 > s2:
            s1 -= queue1[0]
            s2 += queue1[0]
            queue2.append(queue1[0])
            queue1.popleft()
            count += 1
        elif s1 < s2:
            s1 += queue2[0]
            s2 -= queue2[0]
            queue1.append(queue2[0])
            queue2.popleft()
            count += 1
        else:
            break
    return count if count < cnt else -1

"""  재귀함수 이용(시간초과+오답 있음)
queue1 = deque(queue1)
queue2 = deque(queue2)
count = 0
def solution(queue1, queue2):
    global count
    sumq = (sum(queue1)+sum(queue2))
    if sumq % 2 != 0 or max(queue1) > sumq//2 or max(queue2) > sumq//2:
        return -1
    if sum(queue1) > sum(queue2):
        queue2.append(queue1[0])
        queue1.popleft()
        count += 1
        solution(queue1,queue2)
    elif sum(queue1) < sum(queue2):
        queue1.append(queue2[0])
        queue2.popleft()
        count += 1
        solution(queue1,queue2)
    return count
"""