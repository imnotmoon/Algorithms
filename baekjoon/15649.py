# baekjoon 15649

n, m = map(int, input().split())
num = range(1, n+1)
arr = [0] * m
is_used = [0] * (n+1)


def func(i):
    if i == m:
        for j in arr:
            print(j, end=' ')
        print()
        return
    for j in num:
        if is_used[j] == 0:
            arr[i] = j
            is_used[j] = 1
            func(i+1)
            is_used[j] = 0


func(0)
