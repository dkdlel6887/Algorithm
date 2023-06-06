# 장르의 크기 가장 긴 노래 > 장르 내 많이 재생된 노래 > 고유 번호 낮은 노래
# genres : 장르 리스트  / plays : 재생횟수 -> 인덱스: 고유번호


def solution(genres, plays):
    answer = []
    genre_set = list(set(genres))
    genre_dict = {}
    for g in genre_set:
        for p in range(len(plays)):
            if genres[p] == g:
                try:
                    genre_dict[g][0] += plays[p]
                    genre_dict[g].append([plays[p], p])
                except:
                    genre_dict[g] = [plays[p], [plays[p], p]]
    genre_lst = sorted(genre_dict.items(), key=lambda x: -x[1][0])
    genre_final = []
    for g in genre_lst:
        gf = []
        if len(g[1]) > 2:
            for i in range(1, len(g[1])):
                gf.append(g[1][i])
            gf = sorted(gf, key=lambda x: (-x[0], x[1]))
            answer.append(gf[0][1])
            answer.append(gf[1][1])
        else:
            answer.append(g[1][1][1])

    return answer
