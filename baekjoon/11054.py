# baekjoon 11054

N = int(input())
s = list(map(int, input().split()))
left, right = [0 for _ in range(N+2)], [0 for _ in range(N+2)]

for i in range(N):
  t, v = 0, 0
  for j in range(i-1, -1, -1):
    if s[i] > s[j] and left[j+1] > v: t, v = s[j], left[j+1]
  left[i+1] = v+1

for i in range(N-1, -1, -1):
  t, v = 0, 0
  for j in range(i+1, N):
    if s[i] > s[j] and right[j+1] > v: t, v = s[j], right[j+1]
  right[i+1] = v+1

for i in range(1, N+1): left[i] += right[i]
print(max(*left)-1)