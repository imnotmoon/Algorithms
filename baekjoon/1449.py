# baekjoon 1449

n, l = map(int, input().split())
punk = sorted(list(map(int, input().split())))
count = 1
start = punk[0]
for i in range(n):
    if start <= punk[i] <= start+l-1:
        continue
    else:
        start, count = punk[i], count+1

print(count)
