def solution(board, moves):
    answer = 0
    box = []
    for j in moves:
        for i in range(len(board)):
            if board[i][j-1] != 0:
                box.append(board[i][j-1])  # 상자에 추가하고
                board[i][j-1] = 0          # 기존 board는 0으로 변경
                break                      # 1개 꺼내면 다음 move
        if len(box) > 1 and box[-2] == box[-1]:    # 기존거랑 새로 추가한게 같으면
            box.pop()
            box.pop()  # 제일 위 두개 제거
            answer += 2

    return answer
board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))