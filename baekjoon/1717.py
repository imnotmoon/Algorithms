# 1717 - Union Find
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, m = map(int, input().split())
node = list(range(n+1))

def get_parent(a):
    if node[a] == a:
        return a
    node[a] = get_parent(node[a])
    return node[a]

def union(a,b) :
    root_a, root_b = get_parent(a), get_parent(b)
    if a == b:
        return
    node[root_a] = root_b

for i in range(m):
    op, a, b = map(int, input().split())
    if op == 0 : union(a, b)
    elif op == 1 :
        root_a, root_b = get_parent(a), get_parent(b)
        if root_a == root_b:
            sys.stdout.write("YES\n")
        else :
            sys.stdout.write("NO\n")