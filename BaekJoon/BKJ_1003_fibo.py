# 0, 1 이 몇번 출력되는가?
# 0, 1 일때는 1번, 2일때는 2번, 3일때는 3번, 4일때는 (2+3)=5, 5일때는 5+3=8
# 1, -1, 1-1, 1-2, 2-3, 3-5, 5-8, 8-13, ...


tc = int(input())
for _ in range(tc): # 3
    answer = [0,0]
    n = int(input())
    if n == 0:
        answer[0] = 1
    elif n == 1:
        answer[1] = 1
    else:
        answer = [1,1]
        while n > 2:
            tmp = answer[0]
            answer[0] = answer[1]
            answer[1] = answer[0]+tmp
            n-=1
    print(f'{answer[0]} {answer[1]}')
#    d[0] = 1, d[1] = 1 -> d2[0] = d[1], d2[1] = d[0]+d[1] -> d2[1]