# 연산자 우선순위 무시, 나눗셈은 몫만, 음수 나눌 경우 -1 곱한 뒤 계산하고 다시 -1 곱하기
# 최대 최소 값 구하기
import sys
from itertools import permutations

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
operator = list(map(int, sys.stdin.readline().split()))  # + - * / 순서

# max -> / 뒤에는 + , * 뒤에는 -
lst = (
    ["+" for _ in range(operator[0])]
    + ["-" for _ in range(operator[1])]
    + ["*" for _ in range(operator[2])]
    + ["/" for _ in range(operator[3])]
)
print(lst)
operators = list(permutations(lst, n - 1))
print(len(operators))
min_x = 1e9
max_x = -1e9
for o in operators:
    ans = a[0]
    for i in range(n - 1):
        if o[i] == "+":
            ans += a[i + 1]
        elif o[i] == "-":
            ans -= a[i + 1]
        elif o[i] == "*":
            ans *= a[i + 1]
        else:
            if ans >= 0:
                ans = ans // a[i + 1]
            else:
                ans = -1 * ((-1 * ans) // a[i + 1])
    min_x = min(min_x, ans)
    max_x = max(max_x, ans)
print(max_x)
print(min_x)
# pypy3로 겨우 통과..

# python3 bfs / dfs 사용해서 다시 해보기
