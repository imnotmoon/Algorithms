# baekjoon 16562 친구비

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, k = map(int, input().split())
cost = list(map(int, input().split()))
friends = [i for i in range(n+1)]
cost.insert(0,0)

def get_parent(x):
    if friends[x] == x:
        return x
    friends[x] = get_parent(friends[x])
    return friends[x]

def union(a, b):
    a, b = get_parent(a), get_parent(b)
    if a != b:
        friends[a] = b
        cost[b], cost[a] = min(cost[a], cost[b]), 0

for i in range(m):
    # 1. input
    a, b = map(int, input().split())

    # 2. union
    union(a, b)

total = sum(cost)
if total <= k:
    print(total)
else : print("Oh no")
