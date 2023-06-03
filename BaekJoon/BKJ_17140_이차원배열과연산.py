from collections import Counter

r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]


# 원소 개수 같으면 숫자 작은순서, 다르면 개수 적은 순서


def ch_rc(arr):
    if len(arr) >= len(arr[0]):  # r 연산
        mlen = 0
        for a in range(len(arr)):
            ca = Counter(arr[a])
            del ca[0]
            ca = sum(list(sorted(ca.items(), key=lambda x: (x[1], x[0]))), ())
            # a==list, 원소별 개수 나열, dict type
            arr[a] = list(ca)
            mlen = max(len(arr[a]), mlen)
        for a in range(len(arr)):  # 0채워넣기
            if len(arr[a]) != mlen:
                for _ in range(mlen - len(arr[a])):
                    arr[a].append(0)
        return arr
    else:  # c연산
        arr = list(zip(*arr))
        mlen = 0
        for a in range(len(arr)):
            ca = Counter(arr[a])
            del ca[0]
            ca = sum(list(sorted(ca.items(), key=lambda x: (x[1], x[0]))), ())
            # a==list, 원소별 개수 나열, dict type
            arr[a] = list(ca)
            mlen = max(len(arr[a]), mlen)
        for a in range(len(arr)):  # 0채워넣기
            if len(arr[a]) != mlen:
                for _ in range(mlen - len(arr[a])):
                    arr[a].append(0)
        arr = list(zip(*arr))
        return arr

    # for a in range(len(arr)):
    # arr[a] = list(arr[a])


cnt = 0
time = -1
for _ in range(101):
    time += 1
    if r <= len(arr) and c <= len(arr[0]) and arr[r - 1][c - 1] == k:
        cnt += 1
        break
    arr = ch_rc(arr)
if cnt == 0:
    print(-1)
else:
    print(time)
