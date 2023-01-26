#tree1
'''
정점 번호 (V) : 1 ~ (E+1)
간선 수 (E) / 부모-자식 순서 쌍
4
1 2 1 3 3 4 3 5
'''

E = int(input())  # 간선 수: 부모-자식 관계 수
arr = list(map(int, input().split()))
V = E+1   # 정점(노드) 수 = 간선 수+1
root = 1
# 부모를 인덱스로 자식번호 저장
ch1 = [0]*(V+1)
ch2 = [0]*(V+1)

# 자식을 인덱스로 부모번호 저장
par = [0]*(V+1)

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if ch1[p] == 0:
        ch1[p] = c
    else:
        ch2[p] = c
    par[c] = p

def find_root(V):
    for i in range(1, V+1):
        if par[i] == 0:  # 부모가 없으면 root
            return i

def preorder(n):   # VLR: 전위순회, n: root
    if n:
        print(n)   # visit(n) 부모노드 처리
        preorder(ch1[n])  # 왼쪽 자식노드 처리
        preorder(ch2[n])  # 오른쪽 자식노드 처리

def inorder(n):   # LVR: 중위순회, n: root
    if n:
        inorder(ch1[n])  # 왼쪽 자식노드 처리
        print(n)   # visit(n) 부모노드 처리
        inorder(ch2[n])  # 오른쪽 자식노드 처리

def postorder(n):   # LRV: 후위순회, n: root
    if n:
        postorder(ch1[n])  # 왼쪽 자식노드 처리
        postorder(ch2[n])  # 오른쪽 자식노드 처리
        print(n)  # visit(n) 부모노드 처리

#preorder(root)
#inorder(root)
#postorder(root)

print(find_root(V))

# 정점을 주는지, 간선 수를 주는지 문제에따라 V, E 관계를 입력하여 변수로 활용하면 된다.
# 순회를 어떻게 응용하여 사용할지를 생각하며 문제해결을 하면 좋다.

#