# baekjoon 1051

N, M = map(int, input().split())
rect = [ input().rstrip() for _ in range(N) ]

for s in range(min(M, N), -1, -1):
  for i in range(N):
    for j in range(M):
      if i+s < N and j+s < M:
        if rect[i][j] == rect[i][j+s] == rect[i+s][j] == rect[i+s][j+s]:
          print((s+1)**2)
          exit(0)