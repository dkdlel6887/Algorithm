# 각 자리가 등차수열을 이루는 수 2468, 1357
# 1이상 N이하
N = int(input())
if N < 100:
    answer = N
else:
    answer = 99
    for n in range(100,N+1):
        # a = n//100
        # b = n//10 - a*10
        # c = n%10
        # if a-b == b-c:
        #     answer += 1
        if 11*(n//100)-n//10 == n//10-(n//100)*10 - n%10:
            answer += 1
print(answer)



# +) 그냥 풀어보기
# a: 합을 구해야 하는 정수 n개가 저장되어 있는 리스트 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)
# 리턴값: a에 포함되어 있는 정수 n개의 합 (정수)
def solve(a: list) -> int:
    answer = 0
    for n in a:
        answer += n
    return n