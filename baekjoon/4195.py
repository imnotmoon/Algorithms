# baekjoon 4195
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
friends = dict()
number = dict()


def get_parent(a):
    if friends[a] == a:
        return a
    friends[a] = get_parent(friends[a])
    return friends[a]

def union(a, b):
    root_a, root_b = get_parent(a), get_parent(b)
    if root_a != root_b:
        friends[root_b] = root_a
        # ***** 딸려있는 노드 수를 최상위 루트에 더해줌 ***** #
        number[root_a] += number[root_b]
        # ****************************************** #

for i in range(N):
    friends = dict()
    number = dict()
    #1. get f
    F = int(input())
    for f in range(F):
        a, b = map(str, input().split())
        if a not in friends : 
            friends[a] = a
            number[a] = 1
        if b not in friends : 
            friends[b] = b
            number[b] = 1

        #2. union
        union(a,b)

        #3. count number of roots
        print(number[get_parent(a)])