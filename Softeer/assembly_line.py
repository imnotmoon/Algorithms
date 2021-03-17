# 제한시간 : C/C++(1초), Java/Python(2초) | 메모리 제한 : 256MB
# 동일한 자동차를 생산하는 2개의 조립 라인 A와 B가 있다. 두 조립라인에는 각각 N개의 작업장이 있다. 각각의 작업장을 Ai (1 ≤ i ≤ N)와 Bi (1 ≤ i ≤ N)로 표시하자.

# Ai 작업장과 Bi 작업장은 동일한 작업을 수행하지만 작업시간은 다를 수 있다. A 조립 라인의 경우 A1 작업장에서 최초 조립이 시작되고, Ai 작업장에서 작업이 종료되면 바로 Ai+1 작업장에서 작업을 시작할 수 있다.

# B 조립 라인도 동일한 방식으로 조립을 진행한다. Ai 작업장에서 Bi+1작업장으로 혹은 Bi 작업장에서 Ai+1작업장으로 반조립 제품의 이동이 가능(이동시간이 추가됨)할 때 자동차 1대의 가장 빠른 조립 시간을 구하여라.
# 입력형식
# 첫 번째 줄에 작업장의 수 N이 주어진다. i+1 (1 ≤ i ≤ N-1) 번째 줄에는 Ai 작업장의 작업시간, Bi 작업장의 작업시간, Ai 작업장에서 Bi+1 작업장까지 이동시간, Bi 작업장에서 Ai+1 작업장까지 이동시간이 차례로 주어진다. 마지막 N+1번째 줄에는 AN 작업장과 BN 작업장의 작업시간이 주어진다.

# 입력은 다음 조건을 만족한다.

#    1 ≤ N ≤ 103 인 정수
#    각 작업시간과 이동시간은 105을 넘지 않는 양의 정수

import sys
input = sys.stdin.readline

n = int(input())
line = [[] for _ in range(n)]
move_next, move_prev = [], []

for i in range(n):
    tmp = list(map(int, input().split()))
    if i != n-1:
        for j in range(n):
            line[j].append(tmp[j])
        move_next.append(tmp[-2])
        move_prev.append(tmp[-1])
    else:
        for j in range(n):
            line[j].append(tmp[j])

dp = [0 for _ in range(n)]
current, dp[0] = 0, line[0][0]

for i in range(1, n):
    to_next, to_prev = 20000, 20000
    if current+1 < n:
        to_next = dp[i-1] + move_next[current-1] + line[current+1][i]
    if current-1 >= 0:
        to_prev = dp[i-1] + move_prev[current-1] + line[current-1][i]
    stay = dp[i-1] + line[current][i]

    if min(stay, to_next, to_prev) == stay:
        dp[i] = stay
    elif min(stay, to_next, to_prev) == to_next:
        current += 1
        dp[i] = to_next
    else:
        current -= 1
        dp[i] = to_prev

print(dp[n-1])
