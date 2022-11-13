# tree problem

'''
input
11
-1 0 0 1 1 2 2 5 5 7 7
2
5개의 노드, 자식노드를 인덱스로하는 부모노드, 제거할 노드번호(0부터 시작)

7
3 2 -1 2 5 3 5
3
'''
# 예외상황: 루트노드가 지워질때, 0번이 아닌 노드가 루트노드일때
def f(v):
    for i in range(N):
        if par[i] == v:  # 부모 노드가 v인 경우 삭제
            nv = i  # 현재 노드 저장 nv=5
            par[i] = -2  # 삭제
            f(nv)
    par[v] = -2  # 자식노드 모두 제거 후 self값 삭제
#  leaf node 개수 구하기
#  par 집합 내 존재 안하고, 부모노드가 -2가 아닌 애들만 count


N = int(input())  # 노드 개수
par = list(map(int, input().split()))   # 자식노드가 부모로 가지는 노드의 번호
v = int(input())  # 제거할 노드번호
f(v)
cnt = 0
for i in range(N):
    if par[i] != -2 and i not in par:
        cnt += 1
print(cnt)