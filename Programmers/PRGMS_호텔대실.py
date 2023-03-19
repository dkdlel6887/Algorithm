from collections import deque
def solution(book_time):
    answer = 0
    def timeint(t):
        h,m = t.split(":")
        return int(h)*60+int(m)
    # book_time 시간 이른 순서부터 정리
    book_time = sorted(book_time, key = lambda x : x[0])
    print(book_time)
    book_t = []
    for t in book_time:
        book_t.append((timeint(t[0]),timeint(t[1])+10))
    print(book_t)
    que = [book_t[0]]
    
    for b in range(1,len(book_t)):
        cnt = 0
        for q in range(len(que)):
            if que[q][1] <= book_t[b][0]:  # 종료시각이 시작시각보다 이르면
                que[q] = book_t[b]
                # print(f'방추가X{que}')
                cnt+=1
                break
        if cnt==0:
            que.append(book_t[b])
            # print(f'방추가O{que}')
    answer = len(que)
        
    return answer

    
    '''
    for t in book_time:  # 종료시간 전부 10분 추가해주기
        if t[1][3] == '5':  # 종료시간 분단위가 5라면
            # 분단위 변경
            temp2 = list(t[1])
            temp2[3] = '0'
            t[1] = "".join(temp2)
            
            # 시간단위 변경
            temp = list(t[1])  # 종료시간
            temp[1] = str(int(temp[1])+1)
            if len(temp[1]) != 1:
                temp[0] = str(int(temp[0])+1)
                temp[1] = '0'
            t[1] = "".join(temp)
        else:
            temp = list(t[1])
            temp[3] = str(int(temp[3])+1)
            t[1] = "".join(temp)
    '''
    