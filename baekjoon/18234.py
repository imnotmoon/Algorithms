# baekjoon 18234
import sys
input = sys.stdin.readline

N, T = map(int, input().split())
carrots, total = sorted([ list(map(int, input().split())) for _ in range(N) ], key=lambda x:-x[1]), 0
for i in range(len(carrots)): total += carrots[i][0] + (T-i-1) * carrots[i][1]
print(total)