# baekjoon 14501 다시풀기

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
cost = list(map(lambda x: x[1], arr))

for i in range(n):
    upto, pay = arr[i][0], arr[i][1]
    if i + upto > n:
        cost[i] = 0
    for j in range(i+upto, n):
        cost[j] = max(cost[j], cost[i]+arr[j][1])

    # print(cost)

print(max(cost))
