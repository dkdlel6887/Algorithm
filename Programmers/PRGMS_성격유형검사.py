def solution(survey, choices):
    answer = ''
    dict = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    l = len(survey)
    klst = list(dict.keys())  # [R,T,F,C,...]

    # ["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5] : "TCMA"
    for i in range(l):  # 지표의 유형 별 최고점수 저장
        score = abs(4 - choices[i])
        if choices[i] < 4 and dict[survey[i][0:1]] < score:
            dict[survey[i][0:1]] = score
        elif choices[i] > 4 and dict[survey[i][1:0:-1]] < score:
            dict[survey[i][1:0:-1]] = score
    # dict 값을 차례로 2개씩 묶어 그중 큰 값 저장
    for k in range(0, 8, 2):
        if dict[klst[k]] >= dict[klst[k + 1]]:
            answer += klst[k]
        else:
            answer += klst[k + 1]
    # answer+=klst[i] if dict[klst[i]]>=dict[klst[i+1]] else klst[i+1] for i in range(0,8,2)
    return answer
print(solution(["TR", "RT", "TR", "AN"], [7, 1, 3, 2]))

def solution(survey, choices):
    answer = ''
    surveys = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    n = len(survey)
    for i in range(n):
        if choices[i] <= 4:
            surveys[survey[i][:1]] += 4-choices[i]
        else:
            surveys[survey[i][1:]] += choices[i]-4
    if surveys['R'] >= surveys['T']:
        answer += 'R'
    else:
        answer += 'T'
    if surveys['C'] >= surveys['F']:
        answer += 'C'
    else:
        answer += 'F'
    if surveys['J'] >= surveys['M']:
        answer += 'J'
    else:
        answer += 'M'
    if surveys['A'] >= surveys['N']:
        answer += 'A'
    else:
        answer += 'N'
    return answer