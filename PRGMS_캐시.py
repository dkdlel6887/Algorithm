''' 0 <= cacheSize <= 30
    cities = list(input().split())
    len(cities) <= 100000
    for i in range(len(cities)):
        len(cities[i]) <= 20
'''
#LRU, cache 크기만큼 단어저장, 이미있으면 1 없으면 5 총합, 도시명 대소문자 구분 X
def solution(cacheSize, cities):
    len_c = len(cities)
    stack = [0]*cacheSize
    t = 0
    if cacheSize == 0:
        return 5*len_c
    for n in range(len_c):
        cities[n] = cities[n].lower()
    for i in range(len_c):
        if cities[i] in stack:   # 캐시 메모리에 존재하는 경우 해당 원소 삭제 후 제일 뒤 추가
            idx = stack.index(cities[i])
            del(stack[idx])
            stack.append(cities[i])
            t += 1
        else:   # 캐시 메모리에 없는 경우 제일 뒤에 추가 하고 맨앞 원소 제거
            del(stack[0])
            stack.append(cities[i])
            t += 5
    return t