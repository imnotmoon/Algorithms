# 왜 거리 내림차순으로 정렬해서 반씩 나누는건 안되지

import sys
input = sys.stdin.readline

n, m, l = map(int, input().split())
h = sorted(list(map(int, input().split())))
d = [h[0], l-h[-1]-1] + [h[i+1] - h[i] for i in range(len(h)-1)]

left, right, mid = 0, l-1, (l-1)//2
answer = 0
while left <= right:
    count = 0
    for i in range(len(d)):
        if mid < d[i] : count += (d[i]-1) // mid

    if count > m:
        left = mid+1
    else:
        answer = mid
        right = mid-1
    mid = (left+right)//2

print(answer)