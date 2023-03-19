def solution(numbers):
    n = len(numbers)
    answer = [-1]*n
    stack = []
    
    for i in range(n):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    return answer
'''
    for i in range(len(numbers)-1):
        for n in range(i+1,len(numbers)):  
            if numbers[i] < numbers[n]:
                answer[i] = numbers[n]
                break
    return answer
'''