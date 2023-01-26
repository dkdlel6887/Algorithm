'''
#왕실의 나이트 : 나이트가 이동할 수 있는 좌표 개수
# 입력값 a1 출력값 2
knite = list(input().strip())  # a1
abc = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
# ord() : 문자->아스키넘버  a:97
# y = ord(knite[0])-ord('a')
y = abc[knite[0]]
x = int(knite[1])-1
answer = 0
direction = [(2,-1),(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2)]  # 8개 방향
for dy, dx in direction:
    ny = y+dy
    nx = x+dx
    if 0<=ny<8 and 0<=nx<8:
        answer += 1
print(answer)

# 문자열 정렬 + 숫자합 붙이기
string = input()
s_stack = []
n=0
for s in string:
    if s.isalpha():
        s_stack.append(s)
    else:
        n+=int(s)
s_ = "".join(sorted(s_stack))
answer2 = s_+str(n)
print(answer2)
'''
'''
from collections import deque
rows, columns = 6, 6
queries = [[5,1,6,3]]
def solution(rows, columns, queries):
    answer = []
    square_ = [[j for j in range(i * columns + 1, columns * (i + 1)+1)] for i in range(rows)]  # 1,6 / 7,12 / 31, 36
    for k in range(len(queries)):
        print(square_)
        query = [i - 1 for i in queries[k]]
        q = deque()
        q = insert_rotate(q, rows, columns, query)  # 좌표구하기
        lst = deque()
        for y, x in q:  # 좌표에 있는 값들 가져오기
            lst.append(square_[y][x])
        print(lst)
        answer.append(min(lst))  # 최소값 삽입
        lst.rotate(1)  # 시계방향 회전
        n = 0
        for y, x in q:  # 행렬변경
            square_[y][x] = lst[n]
            n += 1

    return answer
def insert_rotate(q, rows, columns, query):
    for y in range(query[0], rows):
        for x in range(query[1], query[3] + 1):
            q.append((y, x))
        break
    for x in range(query[3], columns):
        for y in range(query[0] + 1, query[2] + 1):
            q.append((y, x))
        break
    for y in range(query[2], rows):
        for x in range(query[3] - 1, query[1] - 1, -1):
            q.append((y, x))
        break
    for x in range(query[1], columns):
        for y in range(query[2] - 1, query[0], -1):
            q.append((y, x))
        break
    print(q)
    return q
query = [5,1,6,3]
query = [i - 1 for i in query]
q = deque()
print(insert_rotate(q,rows,columns,query))
#print(solution(rows,columns,queries))
'''


def solution(tickets):
    from collections import defaultdict
    graph = defaultdict(list)
    tickets.sort(key=lambda x: x[1], reverse=True)
    for s, e in tickets:
        graph[s].append(e)

    stack = ["ICN"]
    ans = []
    while stack:
        cur = stack[-1]
        if not graph[cur]:
            ans.append(stack.pop())
        else:
            stack.append(graph[cur].pop())
    return ans[::-1]
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets))