# N개의 숫자카드 중 M개의 숫자 보유중인지 아닌지

# 1<=N,M<=500000, -10^7<=num<10^7
from sys import stdin
N = int(stdin.readline())
N_num = list(map(int, stdin.readline().split()))
M = int(stdin.readline())
M_num = list(map(int, stdin.readline().split()))

"""
# in연산으로 찾는 것이기 때문에 O(n)이 걸림, 따라서 총 시간복잡도는 O(n^2)으로 예상
# 이럴땐 set을 사용하여 문제해결 -> N_num = set(map(int, stdin.readline().split()))
for i in M_num:
    # if i != M_num[M-1]:
    if i in N_num: 
        print(1, end=' ')
    else:
        print(0, end=' ')
"""
# set 없이 이분탐색 이용하여 문제해결
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1
N_num.sort()
nums = ['0']*M
for i in range(M):
    idx = binary_search(N_num, M_num[i], 0, N-1)
    if idx == 1:
        nums[i] = '1'
print(" ".join(nums))
