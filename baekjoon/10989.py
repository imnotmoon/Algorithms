# baekjoon 10989
# Counting Sort + 메모리를 극도로 아낌(count 하나만 씀)
import sys

count = [0]*10001
n = int(sys.stdin.readline())
numbers = []
for i in range(n):
    count[int(sys.stdin.readline())] += 1

for i in range(1, 10001):
    for j in range(count[i]):
        print(i)

