id_list = ["con", "ryan"] #["muzi", "frodo", "apeach", "neo"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"] #["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 3

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report = list(set(report))
    user = {id: [] for id in id_list}  # key=신고받은 id, value=신고한 id

    for i in range(len(report)):
        a, b = report[i].split()
        user[b].append(a)  # 신고받은 id별 신고한 id 저장
    for i in id_list:
        if len(user[i]) >= k:
            for j in user[i]:
                answer[id_list.index(j)] += 1
    return answer  # 각 유저별로 처리 결과 메일을 받은 횟수를 배열에 담아 return

print(solution(id_list, report, k))