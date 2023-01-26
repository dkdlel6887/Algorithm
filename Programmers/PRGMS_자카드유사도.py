def solution(str1, str2):
    answer = 0
    eng = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
           'T', 'U', 'V', 'X', 'Y', 'Z']
    list1, list2 = [], []
    dict1, dict2 = {}, {}
    #    set1, set2 = [], []
    for i in range(len(str1) - 1):
        if str1[i] in eng and str1[i + 1] in eng:
            noun = str1[i] + str1[i + 1]
            list1.append(noun.lower())
    set1 = list(set(list1))
    for j in range(len(set1)):
        cnt = list1.count(set1[j])
        dict1[set1[j]] = cnt
    for i2 in range(len(str2) - 1):
        if str2[i2] in eng and str2[i2 + 1] in eng:
            noun = str2[i2] + str2[i2 + 1]
            list2.append(noun.lower())
    set2 = list(set(list2))
    for j2 in range(len(set2)):
        cnt = list2.count(set2[j2])
        dict2[set2[j2]] = cnt
    # 조기 종료
    if set1 == [] and set2 == []:
        return 65536

    set1 = set(set1)
    set2 = set(set2)
    subset = list(set1.intersection(set2))  # 교집합
    for n in range(len(subset)):
        min_ = min(dict1[subset[n]], dict2[subset[n]])
        for _ in range(min_ - 1):
            subset.append(subset[n])

    totalset = list(set1.union(set2))  # 합집합
    for n in range(len(totalset)):
        dn1, dn2 = 0, 0
        if totalset[n] in set1:
            dn1 = dict1[totalset[n]]
        if totalset[n] in set2:
            dn2 = dict2[totalset[n]]
        max_ = max(dn1, dn2)
        for _ in range(max_ - 1):
            totalset.append(totalset[n])

    answer = int(len(subset) / len(totalset) * 65536)
    return answer
str1, str2 = "abc", "abbb"  #'aa1+aa2','AAAA12'  # 'handshake',	'shake hands'
print(solution(str1,str2))