# baekjoon 18312

N, K = map(int, input().split())
kk = str(K)
result = 0

for i in range(N+1):  # hour
  for j in range(60):  # minute
    for k in range(60):  # second
      if kk in (str(i) if i > 9 else '0'+str(i)) or kk in (str(j) if j > 9 else '0'+str(j)) or kk in (str(k) if k > 9 else '0'+str(k)):
        result += 1

print(result)