# 각 학생이 좋아하는 학생 4명
# 한칸에 학생 한명, 거리가 1인 경우 인접하다고 함
# 인접한 칸(상하좌우)에 좋아하는 번호 있는 경우
# 인접한 칸 빈칸 제일 많은 경우
# 행번호 낮은순, 열번호 낮은순

n = int(input())
students = [list(map(int, input().split())) for _ in range(n**2)]

classroom = [[0] * n for _ in range(n)]

direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

classroom[1][1] = students[0][0]  # 첫번째는 항상 1,1 위치

for s in range(1, len(students)):  # 2 번째 학생부터
    seats = []
    for i in range(n):
        for j in range(n):
            if classroom[i][j] == 0:
                friend = 0
                empty = 0
                for d in direction:
                    y = i + d[0]
                    x = j + d[1]
                    if 0 <= y < n and 0 <= x < n:
                        if classroom[y][x] in students[s][1:]:
                            friend += 1  # 주변에 친구 수 파악
                        elif classroom[y][x] == 0:
                            empty += 1  # 주변 빈 좌석 수 파악
                seats.append([i, j, friend, empty])
    seats = sorted(seats, key=lambda x: (-x[2], -x[3], x[0], x[1]))  # 모든 빈칸 중 우선순위 파악
    classroom[seats[0][0]][seats[0][1]] = students[s][0]
# print(classroom)

score = 0
for i in range(n):
    for j in range(n):
        for s in range(len(students)):
            friend = 0
            if classroom[i][j] == students[s][0]:
                for d in direction:
                    y = i + d[0]
                    x = j + d[1]
                    if 0 <= y < n and 0 <= x < n and classroom[y][x] in students[s][1:]:
                        friend += 1
                if friend == 1:
                    score += 1
                elif friend == 2:
                    score += 10
                elif friend == 3:
                    score += 100
                elif friend == 4:
                    score += 1000
print(score)


"""  시간 차이나는 부분 => append, sorted 안쓰는 방법 360ms -> 160ms
if temp_like > like:
    like, empty = temp_like, temp_empty
    loca = [i, j]
elif temp_like == like and temp_empty > empty:
    like, empty = temp_like, temp_empty
    loca = [i, j]
elif temp_like == like and temp_empty == empty and len(loca) == 0 or loca[0] > i:
    like, empty = temp_like, temp_empty
    loca = [i, j]
elif temp_like == like and temp_empty == empty and len(loca) == 0 or loca[0] == i and loca[1] > j:
    like, empty = temp_like, temp_empty
    loca = [i, j]
"""
