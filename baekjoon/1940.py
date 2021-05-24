# baekjoon 1940

import sys
import copy
input = sys.stdin.readline

n = int(input())
m = int(input())
material = list(map(int, input().split()))
material = sorted(material)

cnt = 0

i, j = 0, len(material)-1
while i < j :
    s = material[i] + material[j]
    if s == m:
        cnt += 1
        i, j = i+1, j-1
    elif s > m :
        j -= 1
    elif s < m :
        i += 1
    

print(cnt)

