T = int(input())

for tc in range(1, T+1):
    n = int(input())
    # r1, c1 / r2, c2 / color   > n회 반복

    arr = [[0 for _ in range(10)] for _ in range(10)]
    for _ in range(n):
        r1, c1, r2, c2, color = map(int, input().split())
        # arr[r1][c1] ~ arr[r2][c2]
        for i in range(r1,r2+1):
            for j in range(c1,c2+1):
                arr[i][j] += 1
    ans = 0
    for i in arr:
        ans += i.count(2)

    print(f'#{tc} {ans}')
"""
[[0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 1, 1, 1, 0, 0, 0, 0],
 [0, 0, 1, 2, 2, 1, 1, 0, 0],
 [0, 0, 1, 2, 2, 1, 1, 0, 0],
 [0, 0, 0, 1, 1, 1, 1, 0, 0],
 [0, 0, 0, 1, 1, 1, 1, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0]]
"""