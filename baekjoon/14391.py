N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

def bf():
  result = 0
  for i in range(1 << N * M):
      total = 0
      for row in range(N):
          srow = 0
          for col in range(M):
              idx = row * M + col
              if i & (1 << idx) != 0: srow = srow * 10 + arr[row][col]
              else:
                  total += srow
                  srow = 0
          total += srow

      for col in range(M):
          scol = 0
          for row in range(N):
              idx = row * M + col
              if i & (1 << idx) == 0: scol = scol * 10 + arr[row][col]
              else:
                  total += scol
                  scol = 0
          total += scol
      result = max(result, total)
  return result

print(bf())