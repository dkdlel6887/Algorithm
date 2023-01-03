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