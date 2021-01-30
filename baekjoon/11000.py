# baekjoon 11000
# heapq
import sys
import heapq
input = sys.stdin.readline

n = int(input())
arr = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x:x[0])
room = []       # use list as min-heap via 'heapq'

count = 0
for i in arr:
    if room and room[0] <= i[0]:
        heapq.heappop(room)     # 리스트(힙)에서 가장 작은(최상단) 원소를 삭제
    heapq.heappush(room, i[1])

print(len(room))