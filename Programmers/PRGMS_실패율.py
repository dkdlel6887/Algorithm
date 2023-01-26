def solution(N, stages):
    answer = []
    # 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 = stages 원소 중 == n(1~N)인 개수 / 스테이지에 도달한 플레이어 수 = stages 원소 중 >= n(1~N)인 개수
    dict = {}
    # 스테이지: 실패율
    for n in range(1, N + 1):
        fail = 0
        total = 0
        for i in stages:
            if i >= n:
                total += 1  # 스테이지 도달한 플레이어 수
                if i == n:
                    fail += 1  # 클리어 못한 플레이어 수
        if total != 0:
            dict[n] = fail / total  # 스테이지별 실패율
        else:
            dict[n] = 0  # {1: 0.9, 2: 0.7, 3: 0.7, 4: 0.8, 5: 0.3}
    answer = sorted(dict, key=lambda x: dict[x], reverse=True)  # sorted(,key)를 거쳐 list 형태로 저장
    '''
    failure = []
    for i in dict:
        failure.append(dict[i])  # 실패율 저장
    failure = sorted(failure)[::-1] # 내림차순 정렬

    for f in failure:
        for i in range(1,N+1):
            if i not in answer and f == dict[i]:  # 작은 번호 스테이지부터 확인하므로 실패율 같은 경우 작은번호 저장
                answer.append(i)
                break
    '''
    return answer  # 실패율 기준 내림차순으로 스테이지의 번호가 담겨있는 배열
N=5
stages=[2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N,stages))
# result = [3,4,2,1,5]