# baekjoon 1976

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())    # n <= 200
m = int(input())    # m <= 1000

city = list(range(n+1))
arr = []
for i in range(n):
    arr.append(list(map(int, input().split()))) 

def get_parent(a):
    if city[a] == a:
        return a
    city[a] = get_parent(city[a])
    return city[a]

def union(a, b) :
    root_a, root_b = get_parent(a), get_parent(b)
    if root_a != root_b:
        city[root_a] = root_b

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            union(i+1,j+1)

# print(city)

travel = list(map(int, input().split()))


res = True
for i in range(len(travel)-1):
    root_a, root_b = get_parent(travel[i]), get_parent(travel[i+1])
    # print(travel[i], travel[i+1])
    # print(root_a, root_b)
    if root_a != root_b:
        res = False
        break

if res: print("YES")
else : print("NO")
