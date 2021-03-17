# 제한시간 : C/C++(1초), Java/Python(2초) | 메모리 제한 : 256MB
# 동일한 자동차를 생산하는 K개의 조립라인 Li (1 ≤ i ≤ K)가 있다. 한 조립라인에는 각각 N개의 작업장이 있다. 각각의 작업장을 Li, j (1 ≤ i ≤ K, 1 ≤ j ≤ N)로 표시하자.

# 모든 라인의 j번째 작업장은 동일한 작업을 수행하지만 작업 시간은 다를 수 있다. 모든 조립라인은 1번 작업장에서 최초 조립이 시작되며, j번째 작업장에서 작업이 종료되면 바로 j+1번째 작업장에서 작업을 시작할 수 있다.

# Li, j 작업장에서 LK, j+1 (i ≠ K) 작업장으로 이동이 가능(이동시간이 추가됨)할 때, 자동차 1대의 가장 빠른 조립 시간을 구하여라.
# 입력형식
# 첫 번째 줄에 라인의 수 K와 작업장의 수 N이 주어진다.
# j+1 (1 ≤ j ≤ N-1) 번째 줄에는 Li, j (1 ≤ i ≤ K) 작업장의 작업시간이 i의 오름차순으로 주어지고, Li, j 작업장에서 LK, j+1 (K ≠ i) 작업장까지 이동시간이 i의 오름차순(i가 동일할 때는 K의 오름차순)으로 주어진다.

# 입력은 다음 조건을 만족한다.

#    1 ≤ N ≤ 102 인 정수
#    1 ≤ K ≤ 102 인 정수
#    각 작업시간과 이동시간은 105을 넘지 않는 양의 정수

import copy
import sys
input = sys.stdin.readline

k, n = map(int, input().split())
line = [[] for _ in range(n)]
move = [[] for _ in range(n)]

for i in range(n):
    tmp = list(map(int, input().split()))
    if i != n-1:
        for j in range(n):
            line[j] = tmp[:n]
        move[i] = tmp[n:]
    else:
        line[i] = tmp

dp = [0 for _ in range(n)]
current, dp[0] = 0, line[0][0]

for i in range(1, n):
    next_line = 20000
    now = copy.deepcopy(current)
    for j in range(k):
        # j : 가려는 라인
        cost = dp[i-1] + line[j][i] + move[now][j]
        if next_line > cost:
            current = j
            print(next_line)
    print()

print(dp[n-1])
