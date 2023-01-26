# 포켓몬 이름 or 번호 맞추기
import sys
# n, m = map(int,input().split()) : takes too long time
n, m = map(int,sys.stdin.readline().split())
infos1 = {}
infos2 = {}
quiz = [0]*m
for i in range(n):
    name = sys.stdin.readline().rstrip()
    infos1[i+1] = name
    infos2[name] = f'{i+1}'
for j in range(m):
    quiz[j] = sys.stdin.readline().rstrip()

for q in quiz:
    try:
        q = int(q)
        print(infos1[q])
    except:
        print(infos2[q])

# 시간 7784ms, 메모리 66444KB  -> 시간 356ms, 메모리 65420KB