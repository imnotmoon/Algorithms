# 1477 다시풀기
n, m, l = map(int, input().split())
t = sorted(list(map(int, input().split())))
dist = [t[0], l-t[-1]-1] + [ t[i+1] - t[i] for i in range(len(t)-1)]

start, end, mid = 0, l-1, (l-1)//2
result = 0
while start <= end:
  cnt = 0
  for d in dist:
    if mid < d : # 이거때문에 답이 달라짐
      cnt += (d-1) // mid
  if cnt > m :
    start = mid+1
  else :
    result = mid
    end = mid-1
  mid = (start+end) // 2

print(result)


