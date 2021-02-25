# baekjoon 2494
import sys
input = sys.stdin.readline

N = int(input())
tmp = list(map(int, input().split()))
towers = [(tmp[i], i+1) for i in range(len(tmp))]
result = [0] * len(towers)

# stack
stack = []
current = N
for i in range(N-1, 0, -1):
    if towers[i][0] <= towers[i-1][0]:  # 막힌 경우
        result[i] = towers[i - 1][1]
        while(stack):
            if stack[-1][0] <= towers[i-1][0]:
                result[stack[-1][1]-1] = towers[i-1][1]
                stack.pop(-1)
            else:
                break
    else:
        stack.append(towers[i])

print(' '.join(list(map(str, result))))
