# baekjoon 8980
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
m = int(input())
boxes = sorted([ list(map(int, input().split())) for _ in range(m) ], key= lambda x:x[1])
available = [0] + [ c for _ in range(n) ]

total = 0
for i in range(m):
    tmp = min(boxes[i][2], *[ available[j] for j in range(boxes[i][0], boxes[i][1]) ])
    total += tmp
    for j in range(boxes[i][0], boxes[i][1]): available[j] -= tmp

print(total)