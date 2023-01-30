def solution(n, stations, w):
    answer = 0
    stack = [0] * n
    for s in stations:
        i = 1
        stack[s - 1] = 1
        for _ in range(w):
            if s - i >= 0:
                stack[s - 1 - i] = 1
            if s + i < n:
                stack[s - 1 + i] = 1
            i += 1
    print(stack)
    # 0이면 깊이 +1, 깊이가 w이고 현위치 값이 0이면 현위치까지 모두 +1, 현위치가 1이면 이전위치 +1
    depth = 0
    for k in range(n):  # 0부터 n-1칸까지 하나씩 확인
        if stack[k] == 0:  # 만약 0: 설치가 안되어있다면
            depth += 1  # 현재 미설치개수 +1하고
            if depth == w + 1:  # 지금까지 미설치개수가 현위치+전파범위와 같으면
                answer += 1  # 1개 설치
                stack[k] = 1  # 설치한걸로 변경: 1
                depth = 0  # 현재 미설치개수를 0으로 초기화
                i = 1
                for _ in range(w):  # 전파범위만큼 설치상태로 변경
                    if k - i >= 0:  # 현위치-i가 리스트 범위 내인지
                        stack[k - i] = 1  # 설치한걸로 변경: 1
                    if k + i < n and stack[k + i] != 1:  # 현위치+i가 리스트 범위 내이고 미설치 상태면 설치
                        stack[k + i] = 1
                    i += 1
                print(stack)
                print(answer)

            elif k == n - 1:  # 마지막칸이면
                stack[k] = 1
                answer += 1
                i = 1
                for _ in range(w):
                    if k - i >= 0 and stack[k - i] != 1:
                        stack[k - i] = 1
                    i += 1
                print(stack)
                print(answer)

        else:  # 현위치에 설치 되어있다면
            if depth > 0:  # 기존에 설치안된부분에 하나설치
                answer += 1
                for d in range(depth, 0, -1):  # 설치안된개수만큼
                    stack[k - d] = 1
                depth = 0
                print(stack)
                print(answer)

    return answer

solution(16,[1,3,5,7,9,],2)
# 효율성 Error -> 계산식을 만들어서 풀어야 효율성 통과
