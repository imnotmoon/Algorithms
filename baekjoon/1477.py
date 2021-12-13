# baekjoon 1477

N, M, L = map(int, input().split())
h = [0] + sorted(list(map(int, input().split()))) + [L]

start, end = 1, L
while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in range(1, len(h)):
        if h[i]-h[i-1] > mid:
            total += (h[i]-h[i-1]-1) // mid
    if total > M : 
        start = mid+1
    else:
        answer = mid
        end = mid-1

print(answer)