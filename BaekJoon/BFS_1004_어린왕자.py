tc = int(input())
# 주어진 원의 좌표안에 출발, 도착점이 포함되는 경우의 수
# 출발, 도착점이 모두 포함되면 0, 하나만 포함되면 1
for _ in range(tc):
    stof = list(map(int,input().split())) # 출발, 도착 좌표
    x = [stof[0],stof[2]]
    y = [stof[1], stof[3]]
    n = int(input())
    answer = 0
    for _ in range(n):
        a,b,r = map(int,input().split())
        if (x[0]-a)**2+(y[0]-b)**2<r**2 and (x[1]-a)**2+(y[1]-b)**2>r**2:
            answer+=1
        elif (x[0]-a)**2+(y[0]-b)**2>r**2 and (x[1]-a)**2+(y[1]-b)**2<r**2:
            answer+=1

    print(answer)