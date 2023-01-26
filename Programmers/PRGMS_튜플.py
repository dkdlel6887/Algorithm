# 셀수있는 수량의 순서있는 열거 또는 어떤 순서를 따르는 요소들의 모음을 튜플(tuple)
#  {  }  ,

# 길이가 짧은 집합부터 앞쪽에 위치, 새로나오는 숫자들은 뒤에 추가, 한번에 두개 문자가 새로 추가 X
s.split(',') > {a},{d,a,c,b},{a,b},{c,a,b,d,e},{a,b,c}
s[0]~s[n] > 각 길이 계산 후 짧은 것부터 나열 > 다음 길이 집합에서 앞에원소 제거 후 추가

def solution(s):
    s_lst = list(s[].split(','))
    for i in range(len(s_lst)):
        s_lst[i] = s_lst.strip('{','}')
    i=0
    while i < len(s_lst)-1:
        if len(s_lst[i]) > len(s_lst[i+1]):
            temp = s_lst[i]
            s_lst[i] = s_lst[i+1]
            s_lst[i+1] = temp
            if i >= 2:
                i -= 2
    # 길이별 정렬된 리스트
    각 원소가 튜플