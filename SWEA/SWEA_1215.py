# 앞뒤가 같은 문자열 찾기, list 자료구조
'''
A A A B
C C B A
A C C A
B A A B
'''

T = 10
for tc in range(1,T+1):
    length = int(input())
    l_len = 8-length+1   # 길이 제한, out of range 오류 발생을 막기 위함
    arr = [input() for _ in range(8)]
    cnt = 0
    for i in range(8):
        for j in range(l_len):
            temp = arr[i][j:j+length]
            if temp == temp[::-1]:
                #print(temp)
                cnt+=1
    for i in range(l_len):
        for j in range(8):
            temp = ''
            for k in range(i,i+length):
                temp += arr[k][j]
            if temp == temp[::-1]:
                #print(temp)
                cnt += 1
    print(f'#{tc} {cnt}')