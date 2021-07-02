# beakjoon 6064
import sys; input = sys.stdin.readline

n = int(input())
for i in range(n):
    found = False
    M, N, x, y = map(int, input().split())
    x, y = x-1, y-1
    ans = -1
    for i in range(x, M*N+1, M):
        if i%N == y:
            ans = i+1
            break
    print(ans)
