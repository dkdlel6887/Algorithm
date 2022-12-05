# 브루투포스, selfnumber
a = 10000
a_lst = [0]*a
for k in range(1, a+1):
    a_lst[k-1] = k
for n in range(1, a):
    nl = len(str(n))  # n의 자릿수
    nplus = 0
    ans = n
    for i in range(nl, 0, -1):
        num = n // 10 ** (i - 1)  # 자릿수 별 숫자
        nplus += num
        n -= num*10**(i-1)
    ans += nplus
    if ans in a_lst:
        a_lst.remove(ans)
for j in a_lst:
    print(j)


# 간소화 된 풀이 for문 개수 2개  N*2 시간
def d(n):
    n += sum(map(int, str(n)))
    return n

noSelfNum = set()  # selfnum이 아닌 수들의 집합

for i in range(1,10001):
    noSelfNum.add(d(i))

for j in range(1,10001):
    if j not in noSelfNum:
        print(j)