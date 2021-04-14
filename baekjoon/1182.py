# baekjoon 1182

n, s = map(int, input().split())
inputs = list(map(int, input().split()))
arr = [0 for _ in range(n)]
numbers = [0 for _ in range(n)]
cnt = 0


def bt(i, idx):
    global cnt
    if sum(numbers) == s and (i, idx) != (0, 0):
        cnt += 1

    if i == n:
        return

    for j in range(idx, len(inputs)):
        if arr[j] == 0:
            arr[j] = 1
            numbers[i] = inputs[j]
            bt(i+1, j)
            arr[j] = 0
            numbers[i] = 0


bt(0, 0)
print(cnt)
