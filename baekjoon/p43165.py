stack = []

def solution(numbers, target):
    answer = 0
    global stack
    # [지금까지 값, 몇번째 수까지 더했는지]가 들어가는 stack
    stack.append([0, 0])
    while(len(stack) > 0) :
        # scenario 1. pop from the stack 
        current = stack[-1]
        stack.pop(-1)
        # scenario 2. push 2 different value to stack with path
        if current[1] == len(numbers) :
            if current[0] == target :
                answer += 1
        else :
            stack.append([current[0] + numbers[current[1]], current[1]+1])
            stack.append([current[0] - numbers[current[1]], current[1]+1])
    return answer