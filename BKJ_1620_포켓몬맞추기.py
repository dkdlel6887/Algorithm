# 포켓몬 이름 or 번호 맞추기
n, m = map(int,input().split())
infos1 = {}
infos2 = {}
quiz = [0]*m
for i in range(n):
    name = input()
    infos1[i+1] = name
    infos2[name] = f'{i+1}'
for j in range(m):
    quiz[j] = input()

for q in quiz:
    try:
        q = int(q)
        print(infos1[q])
    except:
        print(infos2[q])

# 시간 7784ms, 메모리 66444KB