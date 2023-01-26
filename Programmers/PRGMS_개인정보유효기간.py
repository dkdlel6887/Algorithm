def solution(today, terms, privacies):
    answer = []
    term = {}
    lst = []

    for i in terms:
        name, month = i.split()
        term[name] = int(month)
    for i in range(len(privacies)):
        privacies[i] = list(privacies[i].split())  # [날짜, 약관]
        ans = list(map(int, privacies[i][0].split('.')))
        m = ans[1] + term[privacies[i][1]]  # month
        if m > 12:
            ans[0] += m // 12
            ans[1] = m % 12
        else:
            ans[1] = m
        if ans[2] == 1:
            ans[2] = 28
            if ans[1] > 1:  # 2월 이상일 때
                ans[1] -= 1  # 1달 차감
            else:
                ans[1] = 12
                ans[0] -= 1  # 1년 차감
        else:
            ans[2] -= 1  # 1일 차감
        k = ''
        for i in ans:

            if len(str(i)) != 1:
                k += str(i)
            else:
                k += '0'
                k += str(i)
        lst.append(k)  # 기한 적용된 기간값 저장  [yyyy, m, d]

    today = today.replace('.', '')  # yyyymmdd
    for n in range(len(lst)):
        if lst[n] < today:  # 파기
            answer.append(n + 1)
    # 1 약관 시작날짜에서 약관기간을 더한 값이 오늘보다 작으면 정답에 추가
    return answer

print(solution("2022.05.19",["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))