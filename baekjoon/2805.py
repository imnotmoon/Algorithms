import sys
input = sys.stdin.readline

n, m = tuple(map(int, input().split()))
tree = list(map(int, input().split()))
left, right = 0, max(tree)

if sum(tree) == m:
    print(0)
else:
    while(left<right):
        if left+1 == right:
            print(left)
            break
        mid = (left+right)//2
        total = sum([i-mid if mid < i else 0 for i in tree])
        if total > m:
            left = mid
        elif total < m:
            right = mid
        else:
            print(mid)
            break