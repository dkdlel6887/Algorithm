def solution(numbers, hand):
    # [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    answer = ''
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    L = [[3,0]]
    R = [[3,2]]
    for n in numbers:
        i,j = 0,0
        if n in [1, 4, 7]:
            answer += 'L'
            for i in range(4):
                for j in range(3):
                    if n == arr[i][j]:
                        L.append([i, j])
                        break
                if n == arr[i][j]:
                    break
        elif n in [3, 6, 9]:
            answer += 'R'
            for i in range(4):
                for j in range(3):
                    if n == arr[i][j]:
                        R.append([i, j])
                        break
                if n == arr[i][j]:
                    break
        else:
            for i in range(4):
                for j in range(3):
                    if n == arr[i][j]:
                        Li, Lj = abs(i - L[-1][0]), abs(j - L[-1][1])
                        Ri, Rj = abs(i - R[-1][0]), abs(j - R[-1][1])
                        break
                if n == arr[i][j]:
                    break
            if Li + Lj < Ri + Rj or (Li + Lj == Ri + Rj and hand == 'left'):
                answer += 'L'
                L.append([i, j])
            else:  # elif Li+Lj > Ri+Rj or (Li+Lj == Ri+Rj and hand == 'right'):
                answer += 'R'
                R.append([i, j])

    return answer
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'right'))