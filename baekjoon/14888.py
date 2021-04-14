# baekjoon 14888

n = int(input())
numbers = list(map(int, input().split()))
operator = list(map(int, input().split()))    # + - * //
result = []


def func(val, i, current):
    if i == n-1:
        result.append(val)
        return
    for j in range(4):
        if operator[j] > 0:
            operator[j] -= 1
            next_val = calc(val, j, numbers[current+1])
            func(next_val, i+1, current+1)
            operator[j] += 1


def calc(a, idx, b):
    if idx == 0:
        return a+b
    elif idx == 1:
        return a-b
    elif idx == 2:
        return a*b
    elif idx == 3:
        if a < 0:
            a = a*(-1)
            return (a // b) * (-1)
        else:
            return a // b


func(numbers[0], 0, 0)
print(max(result))
print(min(result))
