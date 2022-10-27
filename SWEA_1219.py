# 그래프 문제
def bfs(v, N, t):    # 시작정점, 정점 개수, 목표정점
    visited = [0]*N    #visited 생성 > 이동경로 길이 기록
    q = []
    q.append(v)
    visited[v] == 1

    while len(q) > 0:    # 큐가 비어있지 않으면
        v = q.pop(0)
        if v == t:      # 내가 찾는 목표인지 확인하는 부분
            return 1    # 목표 발견
        for w in adjList[v]:    # v에 인접하고 방문안한 w 인큐, 표시
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[v]+1    # 시작 정점에서 w까지 가는 이동 경로 길이 저장
    return 0
#                / 1 2 3 4 7 10 9
T = 10
for _ in range(T):
    tc, E = map(int, input().split())   # 테스트케이스, 길의 총 개수
    arr = list(map(int,input().split()))   # 순서쌍 입력값

    adjList = [[] for _ in range(100)]
    for i in range(E):
        a, b = arr[i*2], arr[i*2+1]    # 길의 개수 만큼 반복해서  a,b에 (0,1), (2,3),.. 저장
        adjList[a].append(b)    # a가 인접한 정점들 b를 저장

    # print(adjList)
    # print(len(adjList))
    print(f'#{tc} {bfs(0, 100, 99)}')

'''
input
1 16
0 1 0 2 1 4 1 3 4 8 4 3 2 9 2 5 5 6 5 7 7 99 7 9 9 8 9 10 6 10 3 7

output
#1 1

강의 참고해 푼 문제
'''