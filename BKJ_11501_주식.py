from sys import stdin

'''
3
3
10 7 6
3
3 5 9
5
1 1 3 1 2 
'''
# 시간 초과  for문 + max함수 -> 시간복잡도 N^2
def Max_Profit(N, Price):
    profit = 0
    for i in range(N):
        M = max(Price[i:])
        if M > Price[i]:
            temp = Price[i]  # 구매
            # buy(Price[i])  # 자신보다 큰 가격있을 시 구매
            #sell(Price[i] in max(Price[i:]))  # 최대값에서 판대
            profit += M - temp
    return profit

def Profits(N,Price):
    profit = 0
    max_price = 0

    for i in range(N-1, -1, -1):  # (N-1)부터 0까지(-1+1) 1씩 감소
        if Price[i] > max_price:
            max_price = Price[i]
        else:
            profit += max_price-Price[i]  # 최댓값에서 매도
    return profit

T = int(stdin.readline())

for _ in range(T):
    N = int(stdin.readline())
    Price = list(map(int, stdin.readline().split()))
    print(Profits(N,Price))