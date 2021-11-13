# baekjoon 18234
N, T = map(int, input().split())
c, r = sorted([ list(map(int, input().split())) for _ in range(N) ], key=lambda x:-x[1]), 0
for i in range(len(c)): r += c[i][0] + (T-i-1) * c[i][1]
print(r)