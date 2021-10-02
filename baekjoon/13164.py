# baekjoon 13164

n, k = map(int, input().split())
heights = list(map(int, input().split()))
print(sum(sorted([ heights[i+1] - heights[i] for i in range(len(heights)-1) ], reverse=True)[k-1:]))