# baekjoon 1654

import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]
start, mid, end = 1, min(lan), max(lan)


def cut_and_count(mid):
    cnt = 0
    for i in lan:
        cnt += i//mid
    return cnt


mid = (start+end)//2
while(start <= end):
    mid = (start+end)//2
    cnt = cut_and_count(mid)

    if cnt < n:
        end = mid-1
    else:
        start = mid+1

print(end)
