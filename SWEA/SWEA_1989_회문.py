tc = int(input())
words = list(input().strip() for _ in range(tc))

def samsam(word):
    if word[::-1] == word:
        return 1
    else: return 0

for i in range(tc):
    print(f'#{i} {samsam(words[i])}')

