k = int(input())  # 부등호 개수 = 숫자개수 - 1
equalst = list(input().split())
result = []
def backtracking(equalst,idx, numbers, leftnums):
    for num in leftnums:
        if equalst[idx] == '<' and numbers[-1] < num:
            if len(numbers) == k:
                result.append(numbers+[num])
            else:
                backtracking(equalst, idx+1, numbers+[num], leftnums.difference([num]))
        elif equalst[idx] == '>' and numbers[-1] > num:
            if len(numbers) == k:
                result.append(numbers+[num])
            else:
                backtracking(equalst, idx+1, numbers+[num], leftnums.difference([num]))
for i in range(10):
    numbers = []
    leftnums = set([n for n in range(10)])
    backtracking(equalst,0, numbers+[i], leftnums.difference([i]))
max_r = "".join(map(str,max(result)))
min_r = "".join(map(str,min(result)))
print(max_r)
print(min_r)

# 로직
'''
백트래킹 함수 선언
부등호, 부등호 인덱스, 패턴:결과값, 남은숫자
남은숫자 중
만약 부등호가 < 고 패턴마지막게 숫자보다 작으면
   패턴길이가 k:총길이랑 같으면 패턴에 숫자 추가한거 answer에 삽입
   아니면 백트래킹 함수 재귀, 이때 패턴은 숫자추가해주고 남은숫자는 숫자 빼주고, 인덱스는 하나 늘려줌
아니면 부등호가 > 이면 똑같이 진행

1부터 10까지 경우에서 백트래킹 함수 적용하여 진행
정답 모아둔것중에 max, min 찾아서 결과값 출력
'''