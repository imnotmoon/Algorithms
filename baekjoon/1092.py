# baekjoon 1092

import sys
input = sys.stdin.readline

n = int(input())
crane = list(map(int, input().split()))
sorted_crane = sorted(crane, reverse=True)
m = int(input())
box = list(map(int, input().split()))
sorted_box = sorted(box, reverse=True)

# 9 8 6         i
# 7 5 4 2 2     j

time = 0
while sorted_box:
    i, j = 0, 0
    if sorted_crane[i] < sorted_box[j]:
        time = -1
        break
    while i < n and j < len(sorted_box) and sorted_box:
        if sorted_crane[i] >= sorted_box[j]:
            sorted_box.pop(j)
            i += 1
        else:
            j += 1
    time += 1

print(time)
