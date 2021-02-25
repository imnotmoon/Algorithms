# codeforce 1275-A
# https://codeforces.com/problemset/problem/1295/A

t = int(input())
segs = []
for i in range(t):
    segs.append(int(input()))

for seg in segs:
    result = ''
    while(seg > 0):
        if seg == 3:
            result += '7'
            break
        result += '1'
        seg -= 2
    print(result)
