def solution(s):
    numbers = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
               'eight': '8', 'nine': '9'}
    for i in list(numbers.keys()):
        if s.find(i) != -1:
            s = s.replace(i, numbers[i])
    answer = int(s)
    return answer

s = "2three45sixseven"
print(solution(s))