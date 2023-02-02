# 오큰수
from collections import deque
N = int(input())
nge = list(map(int, input().split()))
r_big = [-1]*N
stack = deque([(nge[0],0)])
for i in range(1,N):
    while stack and stack[-1][0] < nge[i]:
        val, idx = stack.pop()
        r_big[idx] = nge[i]
    stack.append((nge[i],i))
print(*r_big)
''' # 메모리를 줄이기 위해 스택에 튜플이 아닌 인덱스만 append
s = [0]  # nge의 index 저장
answer = [-1]*N
for i in range(N):
    while s and nge[s[-1]] < nge[i]:  # 가장 최근에 추가한 인덱스의 원소가 다음원소보다 작으면 pop, while문 통해서 계속 반복
        answer[s.pop()] = nge[i]
    s.append(i)
print(*answer)
'''

# i 랑 i+1이랑 비교해서 작거나같으면 다음으로 크면 pop하고 answer에 i+1 추가, 이전에 작았던것들도 체크하고 전부 pop -> while문
# 시간초과
'''
from collections import deque
N = int(input())
nge = list(map(int, input().split()))
answer = deque()

for i in range(len(nge)):
    cnt = 0
    if i < len(nge)-1:
        for num in nge[i+1:]:
            if num > nge[i]:
                answer.append(num)
                cnt +=1
                break
        if cnt == 0:
            answer.append(-1)
    else:
        answer.append(-1)

answer = " ".join(map(str,answer))
print(answer)
'''