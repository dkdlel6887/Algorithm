def solution(s):
    answer = []
    s = list(s[2:-2].split('},{'))  # len(s)-2는 -2만 적어도 된다.
    s = sorted(s, key=lambda x: len(x))  # ['3', '2,3', '4,2,3', '2,3,4,1']

    s_lst = []
    for n in s:
        s_lst.append(list(map(int, n.split(','))))  # [[3], [2, 3], [4, 2, 3], [2, 3, 4, 1]]

    for i in range(len(s_lst)):
        for j in range(len(s_lst[i])):
            if s_lst[i][j] not in answer:
                answer.append(s_lst[i][j])
                break

    return answer