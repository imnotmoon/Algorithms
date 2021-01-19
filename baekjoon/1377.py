# baekjoon 1377.py

import sys
input = sys.stdin.readline

# input
n = int(input())
arr = []
for i in range(n):
    arr.append((int(input()), i))

sorted_arr = sorted(arr, key=lambda x: x[0])

ret = 0
for i in range(n):
    ret = max(ret, sorted_arr[i][1]-i)
print(ret+1)