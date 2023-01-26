def bfs(v, N):       # v: 시작정점, N: 마지막 정점
    visited = [0]*(N+1)  # visited 생성, 방문 기록용 > 함수 내, 외에 선언할지 문제에 따라 결정
    q = []               # 큐 생성
    q = [v]              # 시적점 enqueue
    visited[v] = 1       # 시작점 처리 표시
    while q:             # 큐가 비어 있지 않으면
        v = q.pop(0)         # dequeue
        print(v)             # visit(v)
        # 인접한 노드 큐에 추가(방문하지 않은)
        for w in adjList[v]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[w]+1


V, E = map(int, input().split())     # V개의 노드, E개의 간선
N = V+1    # N 정점 개수
adjList = [[] for _ in range(N)]
for _ in range(E):
    a, b = map(int, input.split())
    adjList[a].append(b)
    adjList[b].append(a)

bfs(0,V)

