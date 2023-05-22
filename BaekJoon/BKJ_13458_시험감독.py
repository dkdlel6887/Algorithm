import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b, c = map(int, sys.stdin.readline().split())
answer = [0] * len(a)

for i in range(len(a)):
    num = a[i]
    num -= b
    ans = 1
    if num > 0:
        if num % c == 0:
            ans += num // c
        else:
            ans += num // c + 1
    answer[i] = ans

print(sum(answer))
