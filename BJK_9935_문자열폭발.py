import sys

word = list(input().strip())
bomb = list(input().strip())
bomb_len = len(bomb)

stack = []
for i in word:
    stack.append(i)
    if len(stack) >= bomb_len:
        if stack[-bomb_len:] == bomb:
            for _ in range(bomb_len):
                stack.pop()
if len(stack) == 0:
    print("FRULA")
else:
    for n in stack:
        print(n, end="")
""" 시간 초과
def del_bombs(i :int):
    while True:
        if i+bomb_len <= len(word) and word[i:i+bomb_len] == bomb:
            del word[i:i+bomb_len]
            i -= 2
        i += 1
        if i < 0:
            i += 1
        if i == len(word):
            break
    return

del_bombs(0)
if len(word) == 0:
    print('FRULA')
else:
    for i in range(len(word)):
        print(word[i], end="")
"""