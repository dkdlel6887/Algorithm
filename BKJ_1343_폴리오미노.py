def find_X(a):
    if (''.join(a).find('.') != -1 and len(''.join(a).replace('.','')) % 2 == 1) or (''.join(a).find('.') == -1 and len(a) % 2 == 1):
        print(-1)
    else:
        i = 0
        while i < len(a):
            if i+4 <= len(a) and ''.join(a[i:i+4]).find('.') == -1:
                for j in range(i, i+4):
                    a[j] = 'A'
                i += 4
            elif i+2 <= len(a) and ''.join(a[i:i+2]).find('.') == -1:
                for k in range(i, i + 2):
                    a[k] = 'B'
                i += 2
            else:
                i += 1
        print(''.join(a))

s = list(input().strip())
find_X(s)

# 간단한 답..
board = input()

board = board.replace("XXXX", "AAAA")
board = board.replace("XX", "BB")
if 'X' in board:
    print(-1)
else:
    print(board)