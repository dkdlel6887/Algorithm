def solution(new_id):
    nword = list('~!@#$%^&*()=+[{]}:?,<>/'.strip())
    # 대문자>소문자 치환
    new_id = new_id.lower()
    # 알파벳소문자, 숫자, -, _, . 제외 모두 제거
    for i in nword:
        if new_id.find(i) != -1:
            new_id = new_id.replace(i, "")
    # . 2개이상 일때 제거
    while new_id.find('..') != -1:
        new_id = new_id.replace('..', '.')
    # 시작, 끝 위치한 .제거
    if new_id[:1] == '.':
        new_id = new_id[1:]
    if new_id[len(new_id) - 1:] == '.':
        new_id = new_id[:len(new_id) - 1]
    # 빈문자열 a대입
    if new_id == '':
        new_id = 'a'
    # 첫 15글자 제외 제거, 끝자리 '.'이면 제거
    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[14:] == '.':
            new_id = new_id[:14]
    # 2글자 이하라면 마지막문자 복사해서 3글자 만들기
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[len(new_id)-1:]
    answer = new_id

    return answer
lst = ["...!@BaT#*..y.abcdefghijklm", "z-+.^."	, "=.=", "123_.def", "abcdefghijklmn.p"]
for i in lst:
    print(solution(i))