# baekjoon 1107
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
broken = set(map(str, input().split()))
start = 100

min_click = abs(N-start)

if N == start:
    min_click = 0

if len(broken) == 0 :
    min_click = min(len(str(N)), min_click)

def check(num) :
    num = str(num)
    for n in num:
        if n in broken :
            return False
    return True

for i in range(1000001):
    if check(i):
        min_click = min(min_click, len(str(i)) + abs(N-i))

print(min_click)
