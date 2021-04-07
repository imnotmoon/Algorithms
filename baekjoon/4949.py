# baekjoon 4949

while(True):
    line = input()
    if line == '.':
        break

    stack = []
    ret = "yes"
    for i in range(len(line)):
        if line[i] == '[' or line[i] == '(':
            stack.append(line[i])
        elif line[i] == ']':
            if len(stack) > 0:
                if stack[-1] == '[':
                    stack.pop(-1)
                else:
                    ret = "no"
                    break
            else:
                ret = "no"
        elif line[i] == ')':
            if len(stack) > 0:
                if stack[-1] == '(':
                    stack.pop(-1)
                else:
                    ret = "no"
                    break
            else:
                ret = "no"
    if len(stack) > 0:
        print("no")
    else:
        print(ret)
