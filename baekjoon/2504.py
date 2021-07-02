# baekjoon 2504

s = list(input())
stack = []
for i in range(len(s)):
    if s[i] == ')':
        total = 0
        while len(stack) != 0:
            top = stack.pop()
            if top == '(': 
                if total == 0 :
                    stack.append(2)
                else :
                    stack.append(total*2)
                break
            elif top == '[':
                print(0)
                exit(0)
            else :
                total += int(top)
    elif s[i] == ']':
        total = 0
        while len(stack) != 0:
            top = stack.pop()
            if top == '[': 
                if total == 0 :
                    stack.append(3)
                else :
                    stack.append(total*3)
                break
            elif top == '(':
                print(0)
                exit(0)
            else :
                total += int(top)
    else:
        stack.append(s[i])

ret = 0
for i in stack:
    if i == '(' or i == '[':
        print(0)
        exit(0)
    else :
        ret += i
print(ret)