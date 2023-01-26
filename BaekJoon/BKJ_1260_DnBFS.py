N, M, v = map(int,input().split())

adj_lst = [[] for _ in range(N)]

for _ in range(M):
    i, j = map(int,input().split())
    adj_lst[i-1].append(j)       # 노드별 연결노드가 저장됨
    adj_lst[j-1].append(i)

for n in range(N):
    adj_lst[n].sort()
#print(adj_lst)

visited = [0]*N   # [0, 0, 0, 0]
visited_q = [0]*N   # [0, 0, 0, 0]
s = []
q = []
def dfs(v):
    v -= 1
    s.append(v)
    visited[v] = 1
    result = f'{v+1}'
    while s:                        # 스택이 비어있지 않으면
        for w in adj_lst[v]:        # 시작점 v가 연결된 노드들
            w -= 1
            if visited[w] == 0:     # 방문하지 않은 노드일 때
                s.append(w)         # 스택에 w를 쌓는다
                result += f' {w+1}'
                v = w               # 시작점을 w로 변경한다
                visited[v] = 1      # 새로운 시작점을 방문처리 한다
                break
        else:
            s.pop()
            if s:
                v = s[-1]
    print(result)

def bfs(v):
    v -= 1
    q.append(v)
    visited_q[v] = 1
    result = f'{v + 1}'
    while q:
        for w in adj_lst[v]:
            w-=1
            if visited_q[w] == 0:
                q.append(w)
                visited_q[w] = 1
                result += f' {w+1}'
        else:
            q.pop(0)
            if q:
                v = q[0]
    print(result)

dfs(v)
bfs(v)